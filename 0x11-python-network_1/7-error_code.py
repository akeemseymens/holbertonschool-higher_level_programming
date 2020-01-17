#!/usr/bin/python3
"""
Send a GET request to the passed URL and display the body of the response,
printing an error message for HTTP status codes >= 400
"""

if __name__ == '__main__':
    import requests
    from sys import argv

    r = requests.get(argv[1])
    if r.status_code < 400:
        print(r.text)
    else:
        print('Error code: {}'.format(r.status_code))
