import argparse
import collections
import time
import matplotlib.pyplot as plt
import logging


def process(file_path):
    """Open file located in 'file_path' and convert it to string"""
    logging.info(f' Opening input file {file_path}...')
    with open(file_path, 'r') as input_file:
        book = input_file.read()
    logging.info(' Done.')
    return book


def alphabetical(raw_text):
    """Convert a text in an only alphabetical string"""
    logging.info(' Removing all non-alphabetical characters from text...')
    plain_text = ''
    for all_char in raw_text:
        if all_char.isalpha():
            plain_text += all_char
    logging.info(' Done.')
    return plain_text


def histogram(dict_):
    """Create a histogram from data contained in a dict(), showing keys on x-axis"""
    plt.bar(list(dict_.keys()), dict_.values(), color='b')
    plt.show()


if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO)

    start = time.time()

    parser = argparse.ArgumentParser(description='Print some book statistics')
    parser.add_argument('infile', type=str, help='Path to the input file')
    args = parser.parse_args()

    text = alphabetical(process(args.infile).lower())
    total_letters = len(text)

    char = dict(collections.Counter(text))
    sorted_char = dict(sorted(char.items()))

    freq = {}
    for elem in sorted_char:
        freq[elem] = sorted_char[elem]/total_letters

    print('Letters frequencies:')
    for key in freq:
        print(key, '=', round(freq[key]*100, 2), '%')

    logging.warning(' Display a histogram to summarize the results?')
    response = input('Input Y/N:').lower()
    if response == 'y':
        histogram(freq)
    elif response not in 'yn':
        logging.error(' Input character not recognized')

    end = time.time()
    time_ = round(end-start, 2)

    logging.info(f' Measured elapsed time: {time_}sec')
