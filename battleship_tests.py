import unittest

from battleship import ShipError, parse_coords_string, Board, Ship


class BoardTests(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_board_length(self):
        self.assertEqual(len(self.board.grid), 10)
        self.assertEqual(len(self.board.grid[0]), 10)
        self.assertEqual(len(self.board.grid[-1]), 10)

    def test_board_labels(self):
        self.assertEqual(self.board.grid[0][0]['label'], 'A1')
        self.assertEqual(self.board.grid[-1][-1]['label'], 'J10')
        self.assertEqual(self.board.grid[0][0]['mark'], '.')
        self.assertEqual(self.board.grid[-1][-1]['mark'], '.')


class ParseCoordsStringTests(unittest.TestCase):
    def test_coord_parsing(self):
        self.assertEqual(parse_coords_string('A1'), (0, 0))
        self.assertEqual(parse_coords_string('J10'), (9, 9))


class ShipSetupTests(unittest.TestCase):
    def test_ship_setup(self):
        with self.assertRaises(ShipError):
            self.ship = Ship((0, 0), (0, 15), 'Carrier')
        with self.assertRaises(ShipError):
            self.ship = Ship((0, 0), (0, 4, 0), 'Carrier')
        with self.assertRaises(ShipError):
            self.ship = Ship((0, 0), (0, 3), 'Carrier')


class ShipTests(unittest.TestCase):
    def setUp(self):
        self.ship = Ship((0, 0), (0, 4), 'Carrier')

    def test_ship_length(self):
        self.ship = Ship((0, 0), (0, 4), 'Carrier')
        self.assertEqual(self.ship.length, 5)


if __name__ == '__main__':
    unittest.main()