#!/usr/bin/env python3

# Next Prime Number
# Generate prime numbers until 
# the user chooses to stop

def isPrime(x):

	if x == 2:
		return True

	for i in range(2, x):
		if x % i == 0:
			return False
			
	return True

def genPrime(currentPrime):

	newPrime = currentPrime + 1
	
	while True:

		if not isPrime(newPrime):
			newPrime += 1
		else:
			break

	return newPrime

def main():

	currentPrime = 2

	while True:

		answer = input('Would you like to see the next prime? (Y/N) ')

		if answer.lower().startswith('y'):
			print(currentPrime)
			currentPrime = genPrime(currentPrime)

		else:
			break

if __name__ == '__main__':
	main()
