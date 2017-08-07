import argparse


def read_file_lines_count(filepath):
    try:
        f = open(filepath)
        content = f.read()
        return content.count('\n')
    except IOError:
        pass


def main():
    parser = argparse.ArgumentParser(description='file lines counter')
    parser.add_argument('-l', help='file path')
    args = parser.parse_args()
    filepath = vars(args)['l']

    lines_count = read_file_lines_count(filepath)
    if lines_count is not None:
        return '%s %s' % (lines_count, filepath)
    else:
        return 'wc: %s: No such file or directory' % filepath


if __name__ == '__main__':
    print(main())
