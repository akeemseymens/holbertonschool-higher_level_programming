#!/usr/bin/python3
""" Fetch https://intranet.hbtn.io/status using the requests package """

if __name__ == '__main__':
    import requests
    r = requests.get('https://intranet.hbtn.io/status')
    print('Body response:\n\t- type: {}'.format(type(r.text)))
    print('\t- content: {}'.format(r.text))
