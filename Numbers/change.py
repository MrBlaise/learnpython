#!/usr/bin/env python3

# Change Calculator
# Calculates the change for US dollar
# Prints out the type of bills and coins
# that needs to be given to the customer


def changeCoins(change):

    p = 0  # 0.01
    n = 0  # 0.05
    d = 0  # 0.10
    q = 0  # 0.25

    changeCoins = int((change - int(change)) * 100)

    if changeCoins >= 25:
        q = int(changeCoins / 25)
        changeCoins = changeCoins - q * 25

    if changeCoins >= 10:
        d = int(changeCoins / 10)
        changeCoins = changeCoins - d * 10

    if changeCoins >= 5:
        n = int(changeCoins / 5)
        changeCoins = changeCoins - n * 5

    if changeCoins >= 1:
        p = int(changeCoins / 1)

    print('\nPlease give the customer the following coins\n\
Quarters:', q, 'Dimes:', d, 'Nickels:', n, 'Pennies: ', p)


def changeBill(change):

    changeBills = int(change)

    hun = 0
    fif = 0
    twe = 0
    ten = 0
    one = 0

    if changeBills >= 100:
        hun = int(changeBills / 100)
        changeBills = changeBills - hun * 100

    if changeBills >= 50:
        fif = int(changeBills / 50)
        changeBills = changeBills - fif * 50

    if changeBills >= 20:
        twe = int(changeBills / 20)
        changeBills = changeBills - twe * 20

    if changeBills >= 10:
        ten = int(changeBills / 10)
        changeBills = changeBills - ten * 10

    if changeBills >= 1:
        one = int(changeBills / 1)

    print('\nPlease give the customer the following bills:\n',
          'Hundreds: ', hun, ' Fifties: ', fif,
          ' Twenties: ', twe, ' Tens: ', ten, ' Ones: ', one, '\n', sep='')


def changeCalc(cost, money):

    if money < cost:

        change = cost - money

        print('\nPlease pay %.2f$ more\n', change)

    else:

        change = money - cost

        print('\nThe change is: %.2f$\n' % change)

        changeBill(change)
        changeCoins(change)


def main():

    cost = round(float(input('Enter the cost of the purchase: ')), 2)
    money = round(float(input('Enter the money given: ')), 2)

    changeCalc(cost, money)

if __name__ == '__main__':
    main()
