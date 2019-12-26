# pylint: disable=import-error
"""Тест для входного файла"""

import unittest
from src.read_file import create_connect_file


class TestFile(unittest.TestCase):
    """Класс тестов для обработки файла"""
    def incorrect_filename_test(self):
        """Провекрка нахождения файла"""
        with self.assertRaises(FileNotFoundError):
            create_connect_file('invalid file name.txt')

    def incorrect_file_test(self):
        """Проверка состояния файла"""
        with self.assertRaises(IndexError):
            create_connect_file('..\\tests\\test_file.txt')


if __name__ == '__main__':
    unittest.main()
