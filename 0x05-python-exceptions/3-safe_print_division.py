#!/usr/bin/python3


def safe_print_division(a, b):
    try:
        result = a // b
        print("Inside result: {:.1f}".format(result))
    except:
        # if exception occurrs, then result equals to None
        result = None
        print("Inside result: {}".format(result))
    else:
        result = ("{:.1f}".format(result))
    finally:
        return (result)
