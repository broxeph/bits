"""30-minute coding challenge.

Not particularly efficient. Not even sure it works :)
Requirements below.


I would like to add my favorite 6 numbers to consider for a Powerball entry ticket so that I can win 1 billion dollars.

Capture the name of the employees entering the number.
The first 5 favorite numbers will need to be in the range of 1 to 69 and unique. (remember that this is a drawing so
there cannot be duplicates in this range of 5 numbers)
6th favorite number will need to be in the range of 1 to 26 and flagged as the 6th Powerball number.
Keep count of each individual favorite number provided to determine which numbers to use in our final winning number.
(i.e. count the duplicates).
Retrieve the max count of each unique duplicate number and use them as the Powerball numbers.
if there is a tie based on the max counts randomly select the tied number.
Display all employees with their corresponding number entries.
Display the final Powerball number based on the requirements above.

Sample output:
Enter your first name: Wade
Enter your last name: Wilson
select 1st # (1 thru 69): 12
select 2nd # (1 thru 69 excluding 12): 20
select 3rd # (1 thru 69 excluding 12 and 20): 23
select 4th # (1 thru 69 excluding 12, 20, and 23: 56
select 5th # (1 thru 69 excluding 12, 20, 23, and 56: 30
select Power Ball # (1 thru 26): 25

Wade Wilson 15 26 33 60 34 Powerball: 16
Frank Castle 15 26 34 56 61 Powerball: 16

Powerball winning number:
15 26 34 55 63 Powerball: 16
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
            # TODO: Enforce number uniqueness.
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
