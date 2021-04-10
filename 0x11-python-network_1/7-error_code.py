#!/usr/bin/python3
'''module: error'''
import requests
import sys


def main():
    '''main: function takes in a URL, sends a request
    to the URL and displays the body of the response.
    '''

    url = sys.argv[1]
    response = requests.get(url)

    # try if response.raise_for_status is none
    try:
        response.raise_for_status()
        print(response.text)

    # if it is not none handle exceptiion
    except requests.exceptions.HTTPError:
        error_code = response.status_code
        print('Error code:', error_code)


if __name__ == "__main__":
    main()
