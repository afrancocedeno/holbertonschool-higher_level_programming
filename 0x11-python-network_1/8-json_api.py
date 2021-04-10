#!/usr/bin/python3
'''module: json api'''

import requests
import sys


def main():
    '''main: function that takes in a letter and sends a POST request
    to http://0.0.0.0:5000/search_user with the letter as a parameter.
    '''

    # check if no arguments
    if len(sys.argv) == 0:
        print('No result')

    # if arguments
    else:
        url = 'http://0.0.0.0:5000/search_user'
        letter = {'q': sys.argv[1]}
        response = requests.post(url, letter)

        try:
            data = response.json()
            if len(data) == 0:
                print('No result')
            else:
                print('[{}] {}'.format(data['id'], data['name']))
        except ValueError:
            print('Not a valid JSON')


if __name__ == "__main__":
    main()
