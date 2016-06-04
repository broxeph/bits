"""Alex's super great Battleship game. Now with 100% more unit testing!"""

import string


SHIP_TYPES = {
    'Patrol boat': 2,
    'Submarine': 3,
    'Destroyer': 3,
    'Battleship': 4,
    'Carrier': 5
}
MAX_SHIPS = 5

row_labels = string.ascii_uppercase[:10]
col_labels = [str(col) for col in range(1, 11)]


class CoordsError(Exception):
    pass


class BoardError(Exception):
    pass


class ShipError(Exception):
    pass


def parse_coords_string(coords):
    """Parse a coordinate string into row/column tuple."""
    if type(coords) is not str:
        raise CoordsError('Coordinates must be a string value.')
    if not 2 <= len(coords) <= 3:
        raise CoordsError('Coordinates must be length 2 or 3.')
    if coords[0].upper() not in row_labels:
        raise CoordsError('Coordinates must begin with a letter in: ' + ' '.join(row_labels))
    if coords[1:] not in col_labels:
        raise CoordsError('Coordinates must begin with a number in: ' + ' '.join(col_labels))

    return (row_labels.index(coords[0].upper()), col_labels.index(coords[1:]))


def validate_coords(coords):
    if any([type(coords) is not tuple, len(coords) != 2, not 0 <= coords[0] <= 9, not 0 <= coords[1] <= 9]):
        raise CoordsError('Coordinates must be a 2-tuple with values between 0 and 9.')


class Board:
    def __init__(self, ships=None):
        self.grid = []

        for row_label in row_labels:
            row = []

            for col_label in col_labels:
                row.append({
                    'label': row_label + col_label,
                    'mark': '.',
                    'ship': None
                })

            self.grid.append(row)

        self.ships = []
        if ships is None:
            ships = []
        for ship in ships:
            # Add ships to the board.
            if len(ships) >= MAX_SHIPS:
                raise BoardError('{} ships is too many!'.format(len(ships) + 1))

            self.ships.append(ship)

            # TODO: Validate and update grid marks on ship additions.

    def show(self):
        print('  ' + ' '.join(col_labels))
        for row_index, row in enumerate(self.grid):
            print(row_labels[row_index] + ' ' + ' '.join([point['mark'] for point in row]))


class Ship:
    def __init__(self, begin, end, ship_type):
        for point in [begin, end]:
            validate_coords(point)
        if begin[0] != end[0] and begin[1] != end[1]:
            raise ShipError('Ships cannot be placed on diagonals.')

        self.begin = begin
        self.end = end

        if self.length != SHIP_TYPES[ship_type]:
            raise ShipError('Invalid length {0} for ship type {1}: Must be length {2}.'.format(
                self.length, ship_type, SHIP_TYPES[ship_type]))
        if ship_type not in SHIP_TYPES:
            raise ShipError('{} is not a valid ship type.'.format(ship_type))

        self.ship_type = ship_type

    @property
    def length(self):
        return max(abs(self.begin[0] - self.end[0]), abs(self.begin[1] - self.end[1])) + 1

    @property
    def occupied_coords(self):
        """Returns the coords which a ship occupies."""
        coords = []
        for point in range(self.length):
            x = self.begin[0] + (point if self.begin[0] != self.end[0] else 0)
            y = self.begin[1] + (point if self.begin[1] != self.end[1] else 0)
            coords.append((x, y))
        return coords

    def __str__(self):
        return '{0}: {1}-{2}'.format(self.ship_type, self.begin, self.end)

if __name__ == '__main__':
    board = Board()
    board.show()
