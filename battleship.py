"""Alex's super great Battleship game. Now with 100% more unit testing!"""

import string

row_labels = string.ascii_lowercase[:10]
col_labels = [str(col) for col in range(1, 11)]

class Board:
    def __init__(self):
        self.grid = []

        for row_label in row_labels:
            row = []

            for col_label in col_labels:
                row.append({
                    'label': row_label + col_label,
                    'mark': '.'
                })

            self.grid.append(row)

    def show(self):
        print('  ' + ' '.join(col_labels))
        for row_index, row in enumerate(self.grid):
            print(row_labels[row_index].upper() + ' ' + ' '.join([cell['mark'] for cell in row]))


if __name__ == '__main__':
    board = Board()
    board.show()