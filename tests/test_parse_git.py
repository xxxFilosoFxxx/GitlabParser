import unittest
from src.parse_git import parse_git


PATH = 'C:\\Users\\Roman\\FinishedProjects\\GitlabParser\\file.txt'


class TestParse(unittest.TestCase):
    def invalid_token(self):
        token = 'r79F9RqDg34'
        with self.assertRaises(TypeError):
            parse_git(token, PATH)


if __name__ == '__main__':
    unittest.main()
