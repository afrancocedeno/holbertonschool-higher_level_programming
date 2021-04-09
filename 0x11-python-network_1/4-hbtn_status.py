#!/usr/bin/python3
'''module: url status'''
import requests


def main():
    '''main: funciton that fetches https://intranet.hbtn.io/status '''
    response = requests.get('https://intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type:', type(response.text))
    print('\t- utf8 content:', response.text)

if __name__ == "__main__":
    main()
