import unittest
from mock import mock_open, patch

from wc import read_file_lines_count, main


class FileLinesCountTestCase(unittest.TestCase):

    @patch('wc.open', mock_open(read_data='foo\nbar\n'))
    def test_ordinary_file(self, *args):
        self.assertEqual(read_file_lines_count('baz'), 2)

    @patch('wc.open', mock_open(read_data='\n\nbar\n'))
    def test_file_starts_with_empty_line(self, *args):
        self.assertEqual(read_file_lines_count('baz'), 3)

    @patch('wc.open', mock_open(read_data='bar\n\n'))
    def test_file_ends_with_empty_line(self, *args):
        self.assertEqual(read_file_lines_count('baz'), 2)

    @patch('wc.open', mock_open(read_data=''))
    def test_empty_file(self, *args):
        self.assertEqual(read_file_lines_count('baz'), 0)

    @patch('wc.open', mock_open(read_data='\\\nfoo\n'))
    def test_file_contains_backslash(self, *args):
        self.assertEqual(read_file_lines_count('baz'), 2)


class CommandOutputTestCase(unittest.TestCase):

    @patch('wc.vars', return_value={'l': '../a/b/c.txt'})
    @patch('wc.read_file_lines_count', return_value=2)
    def test_existing_filepath(self, *args):
        self.assertEqual(main(), '2 ../a/b/c.txt')

    @patch('wc.vars', return_value={'l': 'c.txt'})
    @patch('wc.read_file_lines_count', return_value=None)
    def test_non_existing_filepath(self, *args):
        self.assertEqual(main(), 'wc: c.txt: No such file or directory')


if __name__ == '__main__':
    unittest.main()
