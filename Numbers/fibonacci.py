#!/usr/bin/env python3

def fibSequence(n):

	assert n > 0

	series = [1]

	while len(series) < n:
		if len(series) == 1:
			series.append(1)
		else:
			series.append(series[-1] + series [-2])

	for i in range(len(series)):
		series[i] = str(series[i])

	return(', '.join(series))

def main():

	print(fibSequence(int(input('How many numbers do you need? '))))

if __name__ == '__main__':
	main()