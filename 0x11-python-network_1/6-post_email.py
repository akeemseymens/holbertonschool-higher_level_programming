#!/usr/bin/python3
"""
Send a POST request to the passed URL with the email as a parameter, and
display the body of the response
"""

if __name__ == '__main__':
    import requests
    from sys import argv

    r = requests.post(argv[1], data={'email': argv[2]})
    print(r.text)
