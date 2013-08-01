#!/usr/bin/env python3

# Change Calculator
# This is the basic of the program
# Later it will be more user-friendly
# And will give more accurate
# answers using cents as well


def changeCalc(cost, money):

    if money < cost:

        print('Please pay ', cost - money, '$ more', sep='')

    else:

        return -1 * (cost - money)


def main():

    cost = int(input('Enter the cost of the item: '))
    money = int(input('Enter the money given: '))

    change = changeCalc(cost, money)

    if type(change) == int:
        print('The change is: ', change, '$', sep='')

if __name__ == '__main__':
    main()
