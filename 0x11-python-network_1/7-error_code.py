#!/usr/bin/python3
'''module: error'''
import requests
import sys


def main():
    '''main: function
    '''

    url = sys.argv[1]

    try:

        response = requests.post(url)
        response.raise_for_status()
        print(response.text)

    except requests.exceptions.HTTPError as response_error:
        print('Error code:', response.status_code)


if __name__ == "__main__":
    main()
