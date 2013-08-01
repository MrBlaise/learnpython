#!/usr/bin/env python3

# Fibonacci Sequence Generator
# Have the user enter a number and
# generate a fibonacci sequence
# which size is equivalent to that number.


def fibSequence(n):
    """
    Generates a fibonacci sequence
    with the size of n
    """
    assert n > 0

    series = [1]

    while len(series) < n:
        if len(series) == 1:
            series.append(1)
        else:
            series.append(series[-1] + series[-2])

    for i in range(len(series)):  # Convert the numbers to strings
        series[i] = str(series[i])

    return(', '.join(series))  # Return the sequence seperated by commas


def main():  # Wrapper function

    print(fibSequence(int(input('How many numbers do you need? '))))

if __name__ == '__main__':
    main()
