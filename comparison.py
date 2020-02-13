"""
Compare jawns.

TODO: Import from Excel (constants unsat)
"""
import antigravity  # For comparison
from pprint import pprint

AYY = (
    ('yup', 'nope', 3),
    ('', '', ''),
    ('yup', 'Nope', 3),
    ('nope', 'nope', 6),
    ('yup', '', 33.6),
)

BEE = (
    ('yup', 'nope', 4),
    ('', 'CowboyNeal', ''),
    ('yup', 'Nope', 3),
    ('Nope', 'nopE', 6),
    ('yup', '', 33.601),
)


def compare(ayy, bee):
    """Compare two tuples of tuples.

    Args:
        ayy (tuple of tuples)
        bee (tuple of tuples)

    Returns:
        see (tuple of tuples)
    """
    see = []
    for ayy_row, bee_row in zip(ayy, bee):
        see_row = []
        for ayy_cell, bee_cell in zip(ayy_row, bee_row):
            if ayy_cell == bee_cell:
                see_cell = ''
            else:
                see_cell = f'Changed: Was "{ayy_cell}", Is "{bee_cell}'
            see_row.append(see_cell)
        see.append(see_row)
    return see

if __name__ == '__main__':
    jawns = compare(AYY, BEE)
    pprint(jawns)
