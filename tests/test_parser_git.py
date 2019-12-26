# pylint: disable=import-error
"""Тест для parser"""

import unittest
from src.parser_git import ParserGit


class TestParserGit(unittest.TestCase):
    """Класс тестов для работы с parser"""
    invalid_token = 'r79F9RqDg'
    path = '..\\file.txt'

    def test_invalid_token(self):
        """Проверка токена"""
        with self.assertRaises(TypeError):
            ParserGit.get_logs(self.path)
            ParserGit.parser_git(self.invalid_token)


if __name__ == '__main__':
    unittest.main()
