#!/usr/bin/python3
'''module: email'''
import requests
import sys


def main():
    '''that takes in a URL and an email address,
    sends a POST request to the passed URL with the email as a parameter,
    and finally displays the body of the response.
    '''
    url = sys.argv[1]
    email = sys.argv[2]
    parameters = {'email': email}

    response = requests.post(url, data=parameters)
    print(response.text)


if __name__ == "__main__":
    main()
