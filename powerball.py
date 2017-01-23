"""30-minute coding challenge.

Not particularly efficient. Not even sure it works :)
"""
from collections import OrderedDict, Counter
from random import randint


TICKET_CHOICES = OrderedDict({
    '1st': 69,
    '2nd': 69,
    '3rd': 69,
    '4th': 69,
    '5th': 69,
    '6th': 26
})


def get_employee_numbers():
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')

    numbers = []
    for ordinal, max_value in TICKET_CHOICES.items():
        while True:
            number = input(f'Select {ordinal} ticket (1 thru 69): ')
            if number.isdigit() and 1 <= int(number) <= max_value:
                break
            print(f'Please enter a number between 1 and {max_value}.')
        numbers.append(number)

    return first_name, last_name, numbers


def jawns():
    """Do all of the things."""
    all_numbers = {}
    more = ''
    while more not in ('n', 'no'):
        first_name, last_name, numbers = get_employee_numbers()
        all_numbers[' '.join((first_name, last_name))] = numbers
        more = input('More employees? (Y/n) ')
        print()

    for employee, numbers in all_numbers.items():
        print(employee, ' '.join(numbers[:5]), 'Powerball:', numbers[5])

    winning_numbers = []
    for i, max_value_allowed in enumerate(TICKET_CHOICES.values()):
        (most_common_number, count) = Counter(numbers[i] for numbers in all_numbers).most_common(1)
        if count > 1:
            winning_numbers.append(randint(1, max_value_allowed))
        else:
            winning_numbers.append(most_common_number)

    print()
    print('Powerball winning number:')
    print(' '.join(winning_numbers[:5]), 'Powerball:', winning_numbers[5])


if __name__ == '__main__':
    jawns()
