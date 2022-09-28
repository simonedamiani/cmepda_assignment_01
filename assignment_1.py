import argparse
import collections


def process(file_path):
    """Open file located in 'file_path' and convert it to string"""
    print(f'Opening input file {file_path}...')
    with open(file_path, 'r') as input_file:
        book = input_file.read()
    print('Done.')
    return book


def alphabetical(raw_text):
    """Convert a text in an only alphabetical string"""
    print('Removing all non-alphabetical characters from text...')
    plain_text = ''
    for all_char in raw_text:
        if all_char.isalpha():
            plain_text += all_char
    print('Done.')
    return plain_text


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Print some book statistics')
    parser.add_argument('infile', type=str, help='Path to the input file')
    args = parser.parse_args()

    text = alphabetical(process(args.infile).lower())
    total_letters = len(text)

    char = dict(collections.Counter(text))
    sorted_char=dict(sorted(char.items()))

    freq = {}
    for elem in sorted_char:
        freq[elem] = sorted_char[elem]/total_letters

    print('Letters frequencies:')
    for key in freq:
        print(key, '=', round(freq[key]*100, 2), '%')