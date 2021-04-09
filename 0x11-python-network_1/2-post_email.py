#!/usr/bin/python3
'''module: post email'''

from urllib import request, parse
import sys


def main():
    ''' main: Python script that takes in a URL and an email, sends a POST request
    in bash:
        curl http://0.0.0.0:5000/post_email -d "email=hr@holbertonschool.com"
    '''
    url = sys.argv[1]
    email = sys.argv[2]
    parameters = {"email": email}

    # pars converts the arguments as the format parameters (=, &)
    data = parse.urlencode(parameters)

    # make the email a byte object string
    data = data.encode('ascii')
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        html = response.read()
        html = html.decode('utf8')
        print(html)

if __name__ == "__main__":
    main()
