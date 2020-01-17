#!/usr/bin/python3
"""
Send a search request to the Star Wars API (swapi.co) and manage pagination
"""

if __name__ == '__main__':
    import requests
    from sys import argv

    r = requests.get('https://swapi.co/api/people/?search={}'.format(argv[1]))
    data = r.json()
    print('Number of results: {}'.format(data.get('count')))
    for person in data.get('results'):
        print(person.get('name'))
    while data.get('next'):
        r = requests.get(data.get('next'))
        data = r.json()
        for person in data.get('results'):
            print(person.get('name'))
