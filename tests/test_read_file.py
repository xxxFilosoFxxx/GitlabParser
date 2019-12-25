import unittest
from src.read_file import create_connect_file


class TestFile(unittest.TestCase):
    def incorrect_filename_test(self):
        with self.assertRaises(FileNotFoundError):
            create_connect_file('invalid file name')

    def incorrect_file_test(self):
        with self.assertRaises(IndexError):
            create_connect_file('..\\tests\\test_file.txt')


if __name__ == '__main__':
    unittest.main()
