#!/usr/bin/python3
'''module header from url'''
from urllib import request
import sys


def main():
    '''get the ramdom http request id'''
    url = sys.argv[1]
    req = request.Request(url)
    with request.urlopen(req) as response:

        # .info() catch all headers information from the request
        the_page_id = response.info()

        # get the randome request header id, source: t.ly/EksZ
        print(the_page_id['X-Request-Id'])

if __name__ == "__main__":
    main()
