#!/usr/bin/python3
import random
number = random.randint(-1000, 10000)
# print("Last digit of", number, "is\n", number % 10)
print("Last digit of {:d} is {:d}".format(number, number % 10 if number > 0 else number % -10))
