# Write out the following functions for now make_process
import os
import string
def clean_word(word):
    '''
    word is a string 
    We need to return a version of the string where all letters have been converted to lowercase, punctuation characters have been removed from both ends but inner punctuation characters have been left alone.
    >>>   clean_word('Hello, World!')
    'hello, world'
    >>> clean_word('Python 3.8')
    'python 3.8'
    '''
    # Strip whitespace and convert to lowercase
    word = word.strip().lower()
    # Remove punctuation from both ends
    while word and word[0] in string.punctuation:
        word = word[1:]
    while word and word[-1] in string.punctuation:
        word = word[:-1]
    return word


'''
Test cases for clean_word function

print(clean_word('Hello, World!'))
print(clean_word('...Python 3.8!!!')) 
print(clean_word('card-board'))       
print(clean_word('  Pearl!  '))

All test cases passed 
'''
   
def average_word_length(text):
    '''
    text is a string
    Return the average word of words in text
    Should not count empty words as words
    Dont include sorrounding punctuation.

    >>> average_word_length('A ball! ball! Big balls! \ What a nice day')
    '''
    words = text.split()
    total_length = 0
    word_count = 0
    for word in words:
        cleaned_word = clean_word(word)
        if cleaned_word:  # Check if the cleaned word is not empty
            total_length += len(cleaned_word)
            word_count += 1
    if word_count == 0:
        return 0
    return total_length / word_count
    
'''
Test cases for average_word_length function

print(average_word_length("A ball! ball! Big balls! What a nice day"))
print(average_word_length("!!! ??? ..."))
print( average_word_length("New\nline\tand\ttabs!"))

All test cases passed

'''

def different_to_total(text):
    '''
    text is a string
    Return the number of unique words in text
    divided by the total number of words in text.
    Should not count empty words as words
    Dont include sorrounding punctuation.

    >>> different_to_total('A ball! ball! Big balls! \ What a nice day')
    '''
    words = text.split()
    unique_words = set()
    total_words = 0
    for word in words:
        cleaned_word = clean_word(word)
        if cleaned_word:  # Check if the cleaned word is not empty
            unique_words.add(cleaned_word)
            total_words += 1
    if total_words == 0:
        return 0
    return len(unique_words) / total_words if total_words > 0 else 0

'''
Test cases for different_to_total function

print(different_to_total("Word word WORD word!"))
print(different_to_total("Hello! Hello, HELLO..."))
print(different_to_total("... !!! ,,,"))

All test cases passed 

'''

def exactly_once_to_total(text):
    '''
    text is a string
    Return the number of words that show up exactly once in text divided by the total number of words in text.
    Should not count empty words as words
    Dont include sorrounding punctuation.

    >>> exactly_once_to_total('A ball! ball! Big balls! \ What a nice day')
    '''
    words = text.split()
    word_count = {}
    total_words = 0
    for word in words:
        cleaned_word = clean_word(word)
        if cleaned_word:  # Check if the cleaned word is not empty
            total_words += 1
            if cleaned_word in word_count:
                word_count[cleaned_word] += 1
            else:
                word_count[cleaned_word] = 1
    if total_words == 0:
        return 0
    exactly_once_count = sum(1 for count in word_count.values() if count == 1)

    # Calculate the ratio of words that appear exactly once to total words
    return exactly_once_count / total_words if total_words > 0 else 0

'''
Test cases for exactly_once_to_total function

print(exactly_once_to_total("A ball! ball! Big balls! What a nice day"))
print(exactly_once_to_total("Pearl! Pearl! Lustrous pearl! Rare. What a nice find."))
print(exactly_once_to_total("Wow, such data. Much wow. Very clean."))
print(exactly_once_to_total("A B C D E F G"))
print(exactly_once_to_total("Hello hello HELLO"))

All test cases passed

'''

def split_string(text, seperators):
    '''
    text is a string
    seperators is a string of seperator characters
    Split the text into a list using any of one of the one character seperators and return the result.
    Remove spaces from the start and end of a string before adding it to the list.
    Do not include empty strings in the list.

    >>> split_spring('A ball! ball! Big balls! What a nice day', ' ')
    ['A', 'ball!', 'ball!', 'Big', 'balls!', 'What', 'a', 'nice', 'day']

    '''
    if not text:
        return []
    # Create a set of separators for faster lookup
    separators_set = set(seperators)
    result = []
    current_word = []
    for char in text:
        if char in separators_set:
            if current_word:  # If we have collected a word
                cleaned_word = ''.join(current_word).strip()
                if cleaned_word:  # Only add non-empty words
                    result.append(cleaned_word)
                current_word = []  # Reset for the next word
        else:
            current_word.append(char)  # Collect characters for the current word
    # Add the last word if there is any
    if current_word:
        cleaned_word = ''.join(current_word).strip()
        if cleaned_word:  # Only add non-empty words
            result.append(cleaned_word)
    return result

'''
Test cases for split_spring function

print(split_string('one*two[three', '* ['))  
print(split_string('A ball! ball! Big balls! What a nice day', ' '))  
print(split_string('A pearl! Pearl! Lustrous pearl! Rare. What a nice find.', ".?!"))  
print(split_string('split,this,string,by,commas', ',')) 
print(split_string('NoSeparatorsHere', ','))  
print(split_string('', ' ,'))  

All test cases passed
'''

def get_sentences(text):
    '''
    text is a string of text
    return a list of sentences from the text.
    sentences are separated by '.', '!', or '?'.
    Use split_string function above

    >>> get_sentences('Hello! How are you? I am fine.')
    ['Hello', 'How are you', 'I am fine']
    '''
    return split_string (text, '.?!')

'''
Test cases for get_sentences function

print(get_sentences('Hello! How are you? I am fine.'))
print(get_sentences('A pearl! Pearl! Lustrous pearl! Rare. What a nice find.'))
print(get_sentences('No punctuation here'))
print(get_sentences(''))

All test cases passed
'''

def average_sentence_length(text):
    '''
    text is a string of text
    return the average number of words per sentence in the text.
    Dont count empty words as words.

    >>> average_sentence_length('Hello! How are you? I am fine.')
    '''
    sentences = get_sentences(text)
    total_words = 0
    total_sentences = 0
    for sentence in sentences:
        words = split_string(sentence, ' ')
        total_words += len(words)
        if words:  # Count only non-empty sentences
            total_sentences += 1
    if total_sentences == 0:
        return 0
    return total_words / total_sentences if total_sentences > 0 else 0

'''
Test cases for average_sentence_length function

print(average_sentence_length('A pearl! Pearl! Lustrous pearl! Rare. What a nice find.'))
print(average_sentence_length('Hello! How are you? I am fine.'))
print(average_sentence_length('Mixing!multiple?punctuation.marks!'))

All test cases passed

'''

def get_phrases(sentence):
    '''
    sentence is a string of text
    return a list of phrases from the sentence.
    phrases are separated by commas, semicolons, or colons.
    Use split_string function above

    >>> get_phrases('Hello, world; this is a test: it works.')
    ['Hello', 'world', 'this is a test', 'it works']
    '''
    return split_string(sentence, ',;:')

'''
Test cases for get_phrases function

print(get_phrases('Hello, world; this is a test: it works.'))
print(get_phrases('No separators here'))
print(get_phrases(',;:Mixed; separators, all:over; the place:'))

All test cases passed
'''

def average_sentence_complexity(text):
    '''
    text is a string of text
    return the average number of phrases per sentence in the text.
    Dont count empty phrases as phrases.

    >>> average_sentence_complexity('Hello, world; this is a test: it works.')
    '''
    sentences = get_sentences(text)
    total_phrases = 0
    total_sentences = 0
    for sentence in sentences:
        phrases = get_phrases(sentence)
        total_phrases += len(phrases)
        if phrases:  # Count only non-empty sentences
            total_sentences += 1
    if total_sentences == 0:
        return 0
    return total_phrases / total_sentences if total_sentences > 0 else 0

'''
Test cases for average_sentence_complexity function

print(average_sentence_complexity('Hello, world; this is a test: it works.'))
print(average_sentence_complexity('A pearl! Pearl! Lustrous pearl! Rare. What a nice find.'))
print(average_sentence_complexity(''))

All test cases passed
'''

def make_signature(text):
    '''
    The signature for text is a list of five elements: 
    
    average word length, different words divided by total words, words used exactly once divided by total words, average sentence length, and average sentence complexity.
    Return the signature for text.

    >>> make signature ('A pearl! Pearl! Lustrous pearl! \
    Rare, what a nice find.")
    [4.1, 0.7, 0.5, 2.5, 1.25]
    '''
    return [
        average_word_length(text),
        different_to_total(text),
        exactly_once_to_total(text),
        average_sentence_length(text),
        average_sentence_complexity(text)
    ]

'''
Test cases for make_signature function

print(make_signature('A pearl! Pearl! Lustrous pearl! Rare, what a nice find.'))
print(make_signature('Hello world! This is a test sentence. Testing, one, two, three!'))
print(make_signature('Repeated repeated repeated words words words.'))

All test cases passed
'''

def get_all_signatures(known_dir):
    '''
    known dir is the name of a directory of books.
    For each file in directory known_dir, determine its signature.
    Return a dictionary where each key is the name of a file, and the value is its signature.
    '''
    signatures = {}
    for filename in os.listdir(known_dir):
        if filename.endswith('.txt'):  # Assuming text files
            file_path = os.path.join(known_dir, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
                signatures[filename] = make_signature(text)
    return signatures


def get_score(signature1, signature2, weights):
    '''
    signature and signature2 are signatures.
    weights is a list of five weights.
    Return the score for signature and signature.
    >>> get_score([4.1, 0.7, 0.5, 2.5, 1.25], \ [4.0, 0.6, 0.4, 2.4, 1.2], \ [1, 1, 1, 1, 1])
    0.1
    '''
    score = 0
    for i in range(len(signature1)):
        score += weights[i] * abs(signature1[i] - signature2[i])
    return score

'''
Test cases for get_score function

print(get_score([1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [1, 1, 1, 1, 1]))
print(get_score([4, 0.5, 0.3, 3, 2], [4, 0.5, 0.3, 3, 2], [1, 1, 1, 1, 1]))
print(get_score([1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [2, 0, 1, 0, 1]))
print(get_score([1.5, 2.5, 3.5, 4.5, 5.5], [0.5, 2.0, 4.0, 5.5, 5.0], [1, 1, 1, 1, 1]))

All test cases passed
'''

def lowest_score(signatures_dict, unknown_signature, weights):
    '''
    signatures dict is a dictionary mapping keys to signatures.
    unknown signature is a signature. weights is a list of five weights.
    Return the key whose signature value has the lowest score with unknown_signature.

    >>> d = ('Dan': [1, 1, 1, 1, 11, 'Leo': [3, 3, 3, 3, 3]}
    >>> unknown = [1, 0.8, 0.9, 1.3, 1.4]
    >>> weights = [11, 33, 50, 0.4, 4]
    >>> lowest score (d, unknown, weights)
    They're easier to we're using our
    "Dan'

    '''
    lowest_key = None
    lowest_score = float('inf')
    for key, signature in signatures_dict.items():
        score = get_score(signature, unknown_signature, weights)
        if score < lowest_score:
            lowest_score = score
            lowest_key = key
    return lowest_key

'''

Test cases for lowest_score function

# Assume get_score and lowest_score have been defined as above

# Test 1: Simple two-author case, uniform weights
d1 = {
    'Dan': [1, 1, 1, 1, 1],
    'Leo': [3, 3, 3, 3, 3]
}
unknown1 = [1, 0.8, 0.9, 1.3, 1.4]
weights1 = [1, 1, 1, 1, 1]
print(lowest_score(d1, unknown1, weights1))
# Expected: 'Dan' (Dan’s signature is much closer to unknown1)

# Test 2: Emphasize the first feature heavily
d2 = {
    'A': [0, 0, 0, 0, 0],
    'B': [1, 1, 1, 1, 1]
}
unknown2 = [0.5, 0.5, 0.5, 0.5, 0.5]
weights2 = [10, 1, 1, 1, 1]
print(lowest_score(d2, unknown2, weights2))
# Expected: 'A'
#  Score_A = 10*0.5 + 4*0.5 = 7.0
#  Score_B = 10*0.5 + 4*0.5 = 7.0
#  Ties go to the first checked key; dictionaries preserve insertion order in Python 3.7+

# Test 3: Single-element dict
d3 = {'Solo': [2, 4, 6, 8, 10]}
unknown3 = [0, 0, 0, 0, 0]
weights3 = [1, 1, 1, 1, 1]
print(lowest_score(d3, unknown3, weights3))
# Expected: 'Solo' (only choice)

# Test 4: Empty dict
d4 = {}
unknown4 = [1, 2, 3, 4, 5]
weights4 = [1, 1, 1, 1, 1]
print(lowest_score(d4, unknown4, weights4))
# Expected: None (no keys to compare)

# Test 5: Multiple authors, non-uniform weights
d5 = {
    'X': [1.0, 2.0, 3.0, 4.0, 5.0],
    'Y': [1.5, 2.5, 3.5, 4.5, 5.5],
    'Z': [0.5, 1.5, 2.5, 3.5, 4.5],
}
unknown5   = [1.2, 2.2, 3.2, 4.2, 5.2]
weights5   = [2,   0.5, 1,   1.5, 0.2]
print(lowest_score(d5, unknown5, weights5))
# Expected: the key whose weighted sum of abs differences is smallest; you can compute:
#   Score_X ≈ 2*0.2 + 0.5*0.2 + 1*0.2 + 1.5*0.2 + 0.2*0.2 = ...
#   Score_Y ≈ ...
#   Score_Z ≈ ...
# And see which is minimal.

All test cases passed

'''

def process_data(mystery_filename, known_dir):
    '''
    mystery filename is the filename of a mystery book whose author we want to know.
    known dir is the name of a directory of books.
    Return the name of the signature closest to the signature of the text of mystery_filename.
    '''
    # Get the signatures of known authors
    known_signatures = get_all_signatures(known_dir)
    # Read the mystery file and compute its signature
    with open(mystery_filename, 'r', encoding='utf-8') as file:
        mystery_text = file.read()
    mystery_signature = make_signature(mystery_text)
    # Define weights for the signature comparison
    weights = [1, 1, 1, 1, 1]  # Equal weights for simplicity
    # Find the author with the closest signature

    closest_author = lowest_score(known_signatures, mystery_signature, weights)

    return closest_author

def make_guess(known_dir):
    '''
    Ask user for a filename.
    Get all known signatures from known dir,
    and print the name of the one that has the lowest score with the user's filename.
    '''
    mystery_filename = input("Enter the filename of the mystery book: ")
    if not os.path.isfile(mystery_filename):
        print(f"File {mystery_filename} does not exist.")
        return None
    try:
        closest_author = process_data(mystery_filename, known_dir)
        print(f"The author of the mystery book '{mystery_filename}' is likely: {closest_author}")
    except Exception as e:
        print(f"An error occurred while processing the file: {e}")
        return None

if __name__ == "__main__":
    known_dir = input("Enter the directory containing known authors' books: ")
    if not os.path.isdir(known_dir):
        print(f"Directory {known_dir} does not exist.")
    else:
        make_guess(known_dir)

# Example usage:
# known_dir = 'path_to_known_authors_directory'
# mystery_filename = 'path_to_mystery_book.txt'
# author = process_data(mystery_filename, known_dir)
# print(f"The author of the mystery book is: {author}")




