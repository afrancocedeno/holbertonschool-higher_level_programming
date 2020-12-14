#!/usr/bin/python3
import random
n = random.randint(-1000, 10000)
# print("Last digit of", n, "is\n", n % 10)
print("Last digit of {:d} is {:d}".format(n, n % 10 if n > 0 else n % -10))
