#!/usr/bin/python3
'''module: url status'''
import urllib.request


def main():
    '''main funciton that fetch internet resources'''
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        print('Body response:')
        print('\t- type:', type(html))
        print('\t- content:', html)

        # how to decode body response, source: t.ly/IKqn
        html = html.decode('utf8')
        print('\t- utf8 content:', html)

if __name__ == "__main__":
    main()
