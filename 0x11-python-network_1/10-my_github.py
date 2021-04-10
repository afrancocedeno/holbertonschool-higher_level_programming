#!/usr/bin/python3
'''module: my github'''

import requests
import sys


def main():
    '''script that takes your GitHub credentials (username
    and password) and uses the GitHub API to display your id
    '''
    username = sys.argv[1]
    password = sys.argv[2]
    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(username, password))

    # try if response.raise_for_status is none
    try:
        response.raise_for_status()
        data = response.json()
        print(data['id'])

    # if it is not none handle exceptiion
    except requests.exceptions.HTTPError:
        print('None')


if __name__ == "__main__":
    main()
