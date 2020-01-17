#!/usr/bin/python3
"""
Send a search request to the Star Wars API
"""

if __name__ == '__main__':
    import requests
    from sys import argv

    r = requests.get('https://swapi.co/api/people/?search={}'
                     .format(argv[1])).json()
    print('Number of results: {}'.format(r.get('count')))
    for person in r.get('results'):
        print(person.get('name'))
        for film in person.get('films'):
            print('\t{}'.format(requests.get(film).json().get('title')))
    while r.get('next'):
        r = requests.get(r.get('next')).json()
        for person in r.get('results'):
            print(person.get('name'))
            for film in person.get('films'):
                print('\t{}'.format(requests.get(film).json().get('title')))
