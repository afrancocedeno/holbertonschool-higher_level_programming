#!/usr/bin/python3
'''module: header'''
import requests
import sys


def main():
    '''main: funciton that takes in a URL, sends a request to
    the URL and displays the value of the variable X-Request-Id
    '''
    url = sys.argv[1]

    response = requests.get(url)
    if 'X-Request-Id' in response:
        print(response.headers['X-Request-Id'])


if __name__ == "__main__":
    main()
