#!/usr/bin/python3
import requests
from sys import argv
import base64

'''
search_twitter - connnecting and search twitter.
'''


def search_twitter(apikey, secret_key, search):
    '''Connect, authenticate, then search'''

    try:

        key = '{}:{}'.format(apikey, secret_key).encode('ascii')
        key = base64.b64encode(key).decode('ascii')
        base_url = 'https://api.twitter.com'
        auth_url = 'https://api.twitter.com/oauth2/token'

        auth_headers = {
            'Authorization': 'Basic {}'.format(b64_encoded_key),
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
        }

        auth_data = {
            'grant_type': 'client_credentials'
        }

        r_auth = requests.post(auth_url, headers=auth_headers, data=auth_data)

        access_token = auth_resp.json()['access_token']

        search_headers = {
            'Authorization': 'Bearer {}'.format(access_token)
        }
        search_params = {
            'q': search,
        }

        search_url = '{}1.1/search/tweets.json'.format(base_url)

        r_resp = requests.get(search_url, headers=search_headers,
                              params=search_params)

        if not r_resp.json().get('statuses'):
            return
        if n >= 5:
            break
        try:
            print("[{}] {} by {}".format(tweet.get('id'),
                                         tweet.get('text'),
                                         tweet.get('user').get('name')))
            n += 1
        except Exception:
            pass
        return r_resp
    except Exception:
        return None

if __name__ == "__main__":
    search_twitter(argv[1], argv[2], argv[3])
