#!/usr/bin/env python3

"""

The following main function is a wrapper function.
It contains the program itself and it will only be
executed if it is not imported to another *.py file

"""

def main(): 

	print('Hello, World!')

"""

The following if statetmant triggers the main function
if it wasn't called by another program, therefore its
__name__ = '__main__' if it was imported into another file
the __name__ would change since it is not the main program
anymore.

"""

if __name__ == '__main__':
	main()