#!/usr/bin/env python3

# The program ask for the user's name
# Greets the user using his name


def main():  # Wrapper function

    name = input('What is your name? ')  # Asks for a string - name

    print('Hello ', name, '! How are you?', sep='', end='\n')

    # PRINT FUNCTION

        # SEP
        # The 'sep' argument in Python 3 will seperate the text
        # with the given character, since now I want an exclamation mark
        # after 'name' I don't like to have any space between that,
        # so I set 'sep' to be nothing.

        # END
        # The 'end' argument is what the program prints
        # after the print statement.
        # By default is '\n' (newline)
        # so you don't need to put that there, however
        # there are some cases when you don't want a newline after
        # every print statement, so this is good to know.


if __name__ == '__main__':
    main()
