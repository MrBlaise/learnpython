#!/usr/bin/env python3


# Fibonacci Value
# Have the user enter a number
# and calculate that number's
# fibonacci value.

def fib(x):
    """
    Assumes x an integer >= 0
    Returns Fibonacci value of x

    """
    assert isinstance(x, int) and x >= 0

    n_1, n_2, i = 1, 1, 2

    while i <= x:
        n_new = n_1 + n_2
        n_1, n_2 = n_2, n_new
        i += 1

    return n_2


def main():  # Wrapper function

    x = int(input('Enter a number to get its fibonacci value: '))

    print('The fibonacci value of', x, 'is:', fib(x))

if __name__ == '__main__':
    main()
