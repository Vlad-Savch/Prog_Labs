import unittest
from src.lab3.sudoku import (group, get_row, get_col, get_block, solve, find_empty_positions,
                             find_possible_values, read_sudoku)


class TestSudoku(unittest.TestCase):
    def test_group_one(self):
        self.assertEqual(group([1, 2, 3, 4], 2), ([[1, 2], [3, 4]]))

    def test_group_two(self):
        self.assertEqual(group([1, 2, 3, 4, 5, 6, 7, 8, 9], 3), ([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

    def test_row_one(self):
        self.assertEqual(get_row([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0)), (['1', '2', '.']))

    def test_row_two(self):
        self.assertEqual(get_row([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 0)), (['4', '.', '6']))

    def test_row_three(self):
        self.assertEqual(get_row([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 0)), (['.', '8', '9']))

    def test_col_one(self):
        self.assertEqual(get_col([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0)), (['1', '4', '7']))

    def test_col_two(self):
        self.assertEqual(get_col([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (0, 1)), (['2', '.', '8']))

    def test_col_three(self):
        self.assertEqual(get_col([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (0, 2)), (['3', '6', '9']))

    def test_block_one(self):
        grid = read_sudoku('../../src/lab3/puzzle1.txt')
        self.assertEqual(get_block(grid, (0, 1)), ['5', '3', '.', '6', '.', '.', '.', '9', '8'])

    def test_block_two(self):
        grid = read_sudoku('../../src/lab3/puzzle1.txt')
        self.assertEqual(get_block(grid, (4, 7)), ['.', '.', '3', '.', '.', '1', '.', '.', '6'])

    def test_block_three(self):
        grid = read_sudoku('../../src/lab3/puzzle1.txt')
        self.assertEqual(get_block(grid, (8, 8)), ['2', '8', '.', '.', '.', '5', '.', '7', '9'])

    def test_solve_puzzle1(self):
        expected_solution = [
            ['5', '3', '4', '6', '7', '8', '9', '1', '2'],
            ['6', '7', '2', '1', '9', '5', '3', '4', '8'],
            ['1', '9', '8', '3', '4', '2', '5', '6', '7'],
            ['8', '5', '9', '7', '6', '1', '4', '2', '3'],
            ['4', '2', '6', '8', '5', '3', '7', '9', '1'],
            ['7', '1', '3', '9', '2', '4', '8', '5', '6'],
            ['9', '6', '1', '5', '3', '7', '2', '8', '4'],
            ['2', '8', '7', '4', '1', '9', '6', '3', '5'],
            ['3', '4', '5', '2', '8', '6', '1', '7', '9']
        ]

        grid = read_sudoku('../../src/lab3/puzzle1.txt')

        self.assertTrue(solve(grid))
        self.assertEqual(grid, expected_solution)

    def test_empty_pos_one(self):
        self.assertEqual(find_empty_positions([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']]), (0, 2))

    def test_empty_pos_two(self):
        self.assertEqual(find_empty_positions([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']]), (1, 1))

    def test_empty_pos_three(self):
        self.assertEqual(find_empty_positions([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']]), (2, 0))

    def test_possible_values_one(self):
        grid = read_sudoku('../../src/lab3/puzzle1.txt')
        values = find_possible_values(grid, (0, 2))
        self.assertEqual(set(values), {'1', '2', '4'})

    def test_possible_values_two(self):
        grid = read_sudoku('../../src/lab3/puzzle1.txt')
        values = find_possible_values(grid, (4, 7))
        self.assertEqual(set(values), {'2', '5', '9'})
