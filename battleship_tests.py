import unittest

from battleship import ShipError, CoordsError, parse_coords_string, Board, Ship


class BoardTests(unittest.TestCase):
    def setUp(self):
        self.board = Board(board_size=10)

    def test_board_length(self):
        self.assertEqual(len(self.board.grid), 10)
        self.assertEqual(len(self.board.grid[0]), 10)
        self.assertEqual(len(self.board.grid[-1]), 10)

    def test_board_labels(self):
        self.assertEqual(self.board.grid[0][0]['label'], 'A1')
        self.assertEqual(self.board.grid[-1][-1]['label'], 'J10')
        self.assertEqual(self.board.grid[0][0]['mark'], ' ')
        self.assertEqual(self.board.grid[-1][-1]['mark'], ' ')

    def test_add_ships(self):
        self.board.add_ships([Ship((1, 1), (1, 5), 'Carrier'), Ship((8, 8), (9, 8), 'Patrol boat')])
        self.assertEqual(len(self.board.ships), 2)


class ParseCoordsStringTests(unittest.TestCase):
    def test_coord_parsing(self):
        self.assertEqual(parse_coords_string('A1'), (0, 0))
        self.assertEqual(parse_coords_string('J10'), (9, 9))


class ShipSetupTests(unittest.TestCase):
    def test_ship_setup(self):
        with self.assertRaises(ShipError):
            self.ship = Ship((0, 0), (0, 15), 'Carrier')
        with self.assertRaises(CoordsError):
            self.ship = Ship((0, 0), (0, 4, 0), 'Carrier')
        with self.assertRaises(ShipError):
            self.ship = Ship((0, 0), (0, 3), 'Carrier')


class ShipTests(unittest.TestCase):
    def setUp(self):
        self.ship = Ship((1, 1), (1, 5), 'Carrier')

    def test_ship_length(self):
        self.assertEqual(self.ship.length, 5)

    def test_ship_occupied_coords(self):
        self.assertEqual(self.ship.points[0], {'coords': (1, 1), 'mark': ' '})
        self.assertEqual(self.ship.points[-1], {'coords': (1, 5), 'mark': ' '})

    def test_ship_hp(self):
        self.assertEqual(self.ship.hp, 5)

    def test_ship_hit(self):
        with self.assertRaises(ShipError):
            self.ship.register_hit((2, 2))
        self.ship.register_hit((1, 3))
        self.assertEqual(self.ship.hp, 4)


if __name__ == '__main__':
    unittest.main()
