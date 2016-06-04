import unittest

import battleship


class BoardSetup(unittest.TestCase):
    def setUp(self):
        self.board = battleship.Board()

    def test_board_length(self):
        self.assertEqual(len(self.board.grid), 10)
        self.assertEqual(len(self.board.grid[0]), 10)
        self.assertEqual(len(self.board.grid[-1]), 10)

    def test_board_labels(self):
        self.assertEqual(self.board.grid[0][0]['label'], 'a1')
        self.assertEqual(self.board.grid[-1][-1]['label'], 'j10')
        self.assertEqual(self.board.grid[0][0]['mark'], '.')
        self.assertEqual(self.board.grid[-1][-1]['mark'], '.')


if __name__ == '__main__':
    unittest.main()