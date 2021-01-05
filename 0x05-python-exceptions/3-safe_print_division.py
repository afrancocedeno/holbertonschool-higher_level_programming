#!/usr/bin/python3


def safe_print_division(a, b):
    result = 0
    try:
        result = a // b
        print("Inside result: {:.1f}".format(result))
    except BaseException as e:
        return ("none")
    finally:
        return ("{:.1f}".format(result))
