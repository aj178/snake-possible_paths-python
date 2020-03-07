from lib.Snakeproblem import *
import unittest


class test_paths_of_snake(unittest.TestCase):

    def test_oneXone_grid(self):
        snake_test = SnakeProblem(1)
        paths = snake_test.possible_paths(1, 1)
        self.assertEqual(paths, 1)

    def test_twoXtwo_grid_snake_four(self):
        snake_test = SnakeProblem(4)
        paths = snake_test.possible_paths("2", "2")
        self.assertEqual(paths, 8)

    def test_twoXtwo_grid_snake_two(self):
        snake_test = SnakeProblem(2)
        paths = snake_test.possible_paths(2, 2)
        self.assertEqual(paths, 8)

    def test_negative_gird_values(self):
        snake_test = SnakeProblem(2)
        paths = snake_test.possible_paths(-2, -2)
        self.assertEqual(paths, "Grid values can't be negative integer.")

    def test_characters_in_grid_values(self):
        snake_test = SnakeProblem(2)
        paths = snake_test.possible_paths("b2", 2)
        self.assertEqual(paths, "Grid value can't be a character or floating point number.")

    def test_negative_snake_length(self):
        snake_test = SnakeProblem(-2)
        paths = snake_test.possible_paths(2, 2)
        self.assertEqual(paths, "Length of snake can't be a negative integer.")

    def test_character_as_snake_length(self):
        snake_test = SnakeProblem("c2")
        paths = snake_test.possible_paths(2, 2)
        self.assertEqual(paths, "Snake length can't be a character or floating point number.")


if __name__ == '__main__':
    unittest.main()
