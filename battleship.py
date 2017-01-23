"""Alex's super great Battleship game. Now with 100% more unit testing!"""

import string


SHIP_TYPES = {
    'Patrol boat': 2,
    'Submarine': 3,
    'Destroyer': 3,
    'Battleship': 4,
    'Carrier': 5
}
ROW_LABELS = string.ascii_uppercase
COL_LABELS = [str(col + 1) for col in range(26)]
DEBUG = True


class CoordsError(Exception):
    pass


class BoardError(Exception):
    pass


class ShipError(Exception):
    pass


def parse_coords_string(coords_string, board_size=26):
    """Parse a coordinate string into row/column tuple."""
    coords_string = coords_string.strip()

    if type(coords_string) is not str:
        raise CoordsError('Coordinates must be a string value.')
    if not 2 <= len(coords_string) <= 3:
        raise CoordsError('Coordinates must be length 2 or 3.')
    if coords_string[0].upper() not in ROW_LABELS[:board_size - 1]:
        raise CoordsError('Coordinates must begin with a letter in: ' + ' '.join(ROW_LABELS[:board_size - 1]))
    if coords_string[1:] not in COL_LABELS[:board_size - 1]:
        raise CoordsError('Coordinates must end with a number in: ' + ' '.join(COL_LABELS[:board_size - 1]))

    coords = (ROW_LABELS.index(coords_string[0].upper()), COL_LABELS.index(coords_string[1:]))
    validate_coords(coords, board_size)

    return coords


def validate_coords(coords, board_size=26):
    """Make sure coords aren't malformed and don't run off the board."""
    if type(coords) is not tuple or \
            len(coords) != 2 or \
            not 0 <= coords[0] <= board_size - 1 or \
            not 0 <= coords[1] <= board_size - 1:
        raise CoordsError('Coordinates must be a 2-tuple with values between 0 and {}.'.format(board_size - 1))


def coords_label(coords):
    """Return alphanumeric label, e.g. 'B4', for given coords 2-tuple."""
    validate_coords(coords)
    return ROW_LABELS[coords[0]] + COL_LABELS[coords[1]]


class Board:
    def __init__(self, board_size=10, ships=None):
        if not 5 <= board_size <= 26:
            raise BoardError("Board size must be between 5 and 26.")
        self.board_size = board_size

        self.grid = []
        for row_label in ROW_LABELS[:self.board_size]:
            row = []

            for col_label in COL_LABELS[:self.board_size]:
                row.append({
                    'label': row_label + col_label,
                    'mark': ' ',
                    'ship': None
                })
            self.grid.append(row)

        if ships is None:
            ships = []
        self.ships = ships

    def add_ships(self, ships):
        for ship in ships:
            for point in ship.points:
                coords = point['coords']
                validate_coords(coords, self.board_size)
                self.grid[coords[0]][coords[1]]['ship'] = ship

            self.ships.append(ship)

    def show(self, show_ships=False):
        print('  ' + ' '.join(COL_LABELS[:self.board_size]))
        for row_index, row in enumerate(self.grid):
            point_characters = []
            for point in row:
                point_characters.append(
                    point['ship'].ship_type[0] if point['ship'] and show_ships else point['mark'])

            print(ROW_LABELS[row_index] + ' ' + ' '.join(point_characters))


class Ship:
    def __init__(self, begin, end, ship_type):
        # Validate endpoints
        for point in [begin, end]:
            validate_coords(point)
        if begin[0] != end[0] and begin[1] != end[1]:
            raise ShipError('Ships cannot be placed on diagonals.')
        self.begin = begin
        self.end = end

        # Validate ship type
        if self.length != SHIP_TYPES[ship_type]:
            raise ShipError('Invalid length {0} for ship type {1}: Must be length {2}.'.format(
                self.length, ship_type, SHIP_TYPES[ship_type]))
        if ship_type not in SHIP_TYPES:
            raise ShipError('{} is not a valid ship type.'.format(ship_type))
        self.ship_type = ship_type

        # Add occupied points
        self.points = []
        for point in range(self.length):
            row = self.begin[0] + (point if self.begin[0] != self.end[0] else 0)
            col = self.begin[1] + (point if self.begin[1] != self.end[1] else 0)
            self.points.append({
                'coords': (row, col),
                'mark': ' '
            })

    @property
    def length(self):
        """Return the ship length as an int."""
        return max(abs(self.begin[0] - self.end[0]), abs(self.begin[1] - self.end[1])) + 1

    def register_hit(self, coords):
        """Add a hit to the appropriate coordinate."""
        if coords not in [point['coords'] for point in self.points]:
            raise ShipError('{0} does not contain a hit for coord {1}'.format(self, coords))
        next(point for point in self.points if point['coords'] == coords)['mark'] = 'X'

    @property
    def hp(self):
        """Return number of non-hit points left in the ship."""
        return sum(1 for point in self.points if point['mark'] == ' ')

    @property
    def status(self):
        """Return hp status or 'Sunk'."""
        return '{0}/{1} hp'.format(self.hp, self.length) if self.hp else 'Sunk!'

    def __str__(self):
        return '{0} - {1}-{2} - {3}'.format(self.ship_type, self.begin, self.end, self.status)


def user_add_ships(board, ships):
    """Prompts the user to add ships to their board."""
    for ship in ships:
        coords = None
        while not coords:
            print()
            input_coords = input("Enter the starting coordinates for your {}: ".format(ship))
            try:
                coords = parse_coords_string(input_coords, board_size=board.board_size)
            except CoordsError as e:
                print("Nope! {}".format(e))
        print("{}? Nice.".format(coords))


if __name__ == '__main__':
    board = Board(board_size=10)
    b = Ship((1, 1), (1, 4), 'Battleship')
    p = Ship((6, 6), (7, 6), 'Patrol boat')
    print(b)
    print(p)
    board.show(show_ships=True)
    board.add_ships([b, p])
    board.show(show_ships=True)

    user_add_ships(board, ['Submarine'])
