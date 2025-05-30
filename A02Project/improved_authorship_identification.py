# The whole program can undergo structural and code improvement
# A no brainer would be to implement it using a class structure 

#!/usr/bin/env python3
import os
import string
import argparse
from typing import List, Dict, Optional

# ─── Text-Signature Utilities 

def clean_word(word: str) -> str:
    """Lowercase `word`, strip leading/trailing punctuation, preserve inner punctuation."""
    w = word.strip().lower()
    # strip leading/trailing punctuation
    while w and w[0] in string.punctuation:
        w = w[1:]
    while w and w[-1] in string.punctuation:
        w = w[:-1]
    return w


def split_on_chars(text: str, seps: str) -> List[str]:
    """
    Split `text` on any character in `seps`, trim whitespace, drop empties.
    """
    if not text:
        return []
    sep_set = set(seps)
    parts: List[str] = []
    buf: List[str] = []
    for ch in text:
        if ch in sep_set:
            chunk = ''.join(buf).strip()
            if chunk:
                parts.append(chunk)
            buf.clear()
        else:
            buf.append(ch)
    # final chunk
    chunk = ''.join(buf).strip()
    if chunk:
        parts.append(chunk)
    return parts


def average_word_length(text: str) -> float:
    words = [clean_word(w) for w in text.split()]
    words = [w for w in words if w]
    if not words:
        return 0.0
    return sum(len(w) for w in words) / len(words)


def type_token_ratio(text: str) -> float:
    """Unique word count / total word count."""
    words = [clean_word(w) for w in text.split() if clean_word(w)]
    if not words:
        return 0.0
    return len(set(words)) / len(words)


def hapax_legomena_ratio(text: str) -> float:
    """Words that occur exactly once / total word count."""
    words = [clean_word(w) for w in text.split() if clean_word(w)]
    if not words:
        return 0.0
    freq: Dict[str,int] = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    once = sum(1 for cnt in freq.values() if cnt == 1)
    return once / len(words)


def get_sentences(text: str) -> List[str]:
    """Split text into sentences on .!?"""
    return split_on_chars(text, '.?!')


def get_phrases(sentence: str) -> List[str]:
    """Split sentence into phrases on ,;:"""
    return split_on_chars(sentence, ',;:')


def average_sentence_length(text: str) -> float:
    sentences = [s for s in get_sentences(text) if s]
    if not sentences:
        return 0.0
    word_counts = [len(s.split()) for s in sentences]
    return sum(word_counts) / len(sentences)


def average_sentence_complexity(text: str) -> float:
    sentences = [s for s in get_sentences(text) if s]
    if not sentences:
        return 0.0
    phrase_counts = [len(get_phrases(s)) for s in sentences]
    return sum(phrase_counts) / len(sentences)


def make_signature(text: str) -> List[float]:
    """
    Compute the 5-element signature of `text`:
      [avg_word_len, type_token_ratio, hapax_legomena_ratio,
       avg_sentence_length, avg_sentence_complexity]
    """
    return [
        average_word_length(text),
        type_token_ratio(text),
        hapax_legomena_ratio(text),
        average_sentence_length(text),
        average_sentence_complexity(text),
    ]


# ─── Author-Attribution Core 

def get_all_signatures(known_dir: str) -> Dict[str, List[float]]:
    """Read every .txt file in `known_dir` and return {filename: signature}."""
    sigs: Dict[str, List[float]] = {}
    for fname in os.listdir(known_dir):
        if not fname.lower().endswith('.txt'):
            continue
        path = os.path.join(known_dir, fname)
        with open(path, 'r', encoding='utf-8') as f:
            sigs[fname] = make_signature(f.read())
    return sigs


def score_signature(sig1: List[float], sig2: List[float], weights: List[float]) -> float:
    """Compute weighted sum of absolute differences between two signatures."""
    return sum(w * abs(a - b) for a, b, w in zip(sig1, sig2, weights))


def find_best_match(
    mystery_sig: List[float],
    known_sigs: Dict[str, List[float]],
    weights: List[float]
) -> Optional[str]:
    """Return the filename whose signature is closest to `mystery_sig`."""
    best_key: Optional[str] = None
    best_score = float('inf')
    for key, sig in known_sigs.items():
        sc = score_signature(sig, mystery_sig, weights)
        if sc < best_score:
            best_score, best_key = sc, key
    return best_key


def process_data(mystery_path: str, known_dir: str, weights: List[float]) -> Optional[str]:
    """
    Read `mystery_path`, compute its signature, compare to known_dir,
    and return the best-matching filename (or None if no files).
    """
    if not os.path.isfile(mystery_path):
        raise FileNotFoundError(f"Mystery file not found: {mystery_path}")
    known_sigs = get_all_signatures(known_dir)
    if not known_sigs:
        return None
    with open(mystery_path, 'r', encoding='utf-8') as f:
        mystery_sig = make_signature(f.read())
    return find_best_match(mystery_sig, known_sigs, weights)


# ─── CLI Entrypoint 

def main():
    p = argparse.ArgumentParser(description="Attribution via text signatures")
    p.add_argument('known_dir', help="Directory of known-author .txt files")
    p.add_argument('mystery_file', help="Path to the mystery .txt file")
    p.add_argument(
        '--weights',
        nargs=5,
        type=float,
        default=[1,1,1,1,1],
        help="Five weights for the signature dimensions"
    )
    args = p.parse_args()

    try:
        author = process_data(args.mystery_file, args.known_dir, args.weights)
        if author:
            print(f"Likely author: {author}")
        else:
            print("No known signatures found to compare against.")
    except Exception as e:
        print(f"Error: {e}")
        exit(1)


if __name__ == '__main__':
    main()




