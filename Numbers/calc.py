#!/usr/bin/env python3

# Calculator
# Have the user enter 2 number - a. b -
# and an operator - op - and calculate
# the solution - c - according to the
# type of the given operator


def calc(a, b, op):
    """
    Returns a string like this: a op b = c
    where c is the computed value according to the opeartor
    """

    if op not in '+-/*':
        return 'Please only type one of these characters: "+, -, *, /"!'

    if op == '+':
        return(str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a + b))
    if op == '-':
        return(str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a - b))
    if op == '*':
        return(str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a * b))
    if op == '/':
        return(str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a / b))


def main():  # Wrapper function

    a = int(input('Please type the first number: '))
    b = int(input('Please type the second number: '))
    op = input(
        'What kind of operation would you like to do?\
        \nChoose between "+, -, *, /" : ')

    print(calc(a, b, op))

if __name__ == '__main__':
    main()
