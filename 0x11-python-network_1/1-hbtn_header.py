#!/usr/bin/python3
'''  value of the X-Request-Id variable found in the header of the response.'''


if __name__ == '__main__':
    import urllib.request
    from sys import argv
    with urllib.request.urlopen(argv[1]) as response:
        xreq_id = response.getheader('X-request-ID')
    print(xreq_id)
