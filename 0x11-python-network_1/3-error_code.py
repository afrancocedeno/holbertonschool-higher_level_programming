#!/usr/bin/python3
''' module: error code '''

from urllib.request import Request, urlopen
from urllib.error import HTTPError
import sys


def main():
    ''' main: script that takes in a URL, sends a request
    to the URL and displays the body of the response
    '''

    url = sys.argv[1]
    req = Request(url)
    try:
        with urlopen(req) as response:
            html_content = response.read()
            html_content = html_content.decode('utf8')
            print(html_content)
    except HTTPError as response_error:
        print('Error code:', response_error.code)

if __name__ == "__main__":
    main()
