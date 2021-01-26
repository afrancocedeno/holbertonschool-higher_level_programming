#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10


def checker_digit(self):
    if self > 5:
        return (' and is greater than 5')
    if self == 0:
        return (' and is 0')
    if self < 6 and not 0:
        return (' and is less than 6 and not 0')


dch = checker_digit(last_digit)
print('Last digit of ' + str(number) + ' is ', str(last_digit) + dch)
