#!/usr/bin/env python3

# Prime Factorization
# Have the user enter a number
# and return its prime factors

# Extra: show the exponent of
# the prime factors as well

from collections import Counter

def isPrime(x):

	if x == 2:
		return True

	for i in range(2, x+1):
		if x % i == 0:
			return False
		else:
			return True

def getExponent(n):

	c = Counter(n)
	factors = []

	for i in range(min(n), max(n)+1):
		if i in n:
			if c[i] != 1:
				factors.append(str(i)+'^'+str(c[i]))
			else:
				factors.append(str(i))

	return factors


def main(): # Wrapper function

	n = int(input('Enter a number to find its prime factors: '))

	factors = []
	counter = 1

	while True:

		if n == 1 or n == 0:
			break

		for i in range(counter, n+1):
			if n % i == 0:
				if isPrime(i):
					factors.append(i)
					n //= i
					break
		if n == 1:
			break

	if len(factors) != 0:
		factors = getExponent(factors)
		print(', '.join(factors))
	else:
		print('The number', n, 'does not have any prime factors.')

if __name__ == '__main__':
	main()