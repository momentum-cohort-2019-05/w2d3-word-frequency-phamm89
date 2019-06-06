STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    pass


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)

import re
import string
# Determines how many lines are in the file
with open(file) as text_file:
    lines = len(text_file.readlines())
    print(f"{lines} lines in the file.")

# Store text file as a string
# Change uppercase to lowercase and remove punctuation 
document_file = open(file, 'r')
text_string = document_file.read().lower().replace(",","").replace(".","").replace(":","").replace("!","").replace(";","").replace("-","").replace("'","")
print(text_string)

# Separate words in text file
individual_words = text_string.split()

# Remove stopwords from text file
remaining_words = [word for word in individual_words if word not in STOP_WORDS]
remaining = ' '.join(remaining_words)

# Print text file without stopwords
text_string = remaining.split()
print(text_string)

# Blank list
frequency = {}

# Count frequency of words
for word in text_string:
    if word not in frequency:
        frequency[word] = 0
    frequency[word] += 1
    
# Given a sequence of items, return the second item of that sequence
def get_second_item(seq):
    return seq[1]

# Sort the list by the second item 
frequency_list = sorted(frequency.keys(), key=get_second_item)

# Print words:frequency
for words in frequency_list:
    print('Word: ' + str(words) + '  | Frequency: ' + str(frequency[words]) + str(frequency[words] * ' *'))
