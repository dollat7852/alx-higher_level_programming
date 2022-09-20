#!/usr/bin/python3

def _fizzbuzz(n):
    """Returns the Fizz Buzz value of a number"""
    if not n % 3 and not n % 5:
        print("FizzBuzz", end=' ')
    elif not n % 3:
        print("Fizz", end=' ')
    elif not n % 5:
        print('Buzz', end=' ')
    else:
        print(n, end=' ')


def fizzbuzz():
    for i in range(1, 101):
        _fizzbuzz(i)
