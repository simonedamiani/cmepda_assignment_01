import argparse

def process(file_path):
    """Open file located in 'file_path' and convert it to string"""
    print(f'Opening input file {file_path}...')
    with open(file_path, 'r') as input_file:
        text = input_file.read()
    print('Done.')



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Print some book statistics')
    parser.add_argument('infile', type=str, help='Path to the input file')
    args = parser.parse_args()
    process(args.infile)