#!/usr/bin/env python3

# Tax calculator
# This program currently
# only works with the hungarian tax

def calcTax(cost, country='hungary'):

    countries = {'hungary' : 27}

    if country in countries.keys():
        tax = (cost / 100) * countries[country]
    else:
        return "Country can't be found"

    return tax

def main(): # Wrapper function

    tax = calcTax(int(input('What was the cost of your purchase? ')),
    input('Which country are you in? '))

    if type(tax) == str:
    	print(tax)
    else:
    	print('The tax on your purchase was:', tax)

if __name__ == '__main__':
 	main()