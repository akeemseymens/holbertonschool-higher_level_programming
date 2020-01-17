#!/usr/bin/python3
""" Fetch the value of the X-Request-ID variable found in the header """

if __name__ == '__main__':
    import requests
    from sys import argv
    r = requests.get(argv[1])
    print(r.headers.get('X-Request-ID'))
