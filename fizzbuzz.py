import random

SEQUENCE = range(1,21)


def this_way():
    """Do it this way."""
    for i in SEQUENCE:
        if i % 15 == 0:
            print('fizzbuzz')
        elif i % 3 == 0:
            print('fizz')
        elif i % 5 == 0:
            print('buzz')
        else:
            print(i)


def that_way():
    """Do it that way."""
    for i in SEQUENCE:
        output = ''
        if i % 3 == 0:
            output += 'fizz'
        if i % 5 == 0:
            output += 'buzz'
        if not output:
            output = i
        print(output)


if __name__ == '__main__':
    if random.getrandbits(1):
        this_way()
        print('(This way)')
    else:
        that_way()
        print('(That way)')
