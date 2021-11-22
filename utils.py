import json
import os
import urllib.parse
import urllib.request
from getpass import getpass

import requests
from requests.compat import urljoin


BASE_API_URL = 'https://api.themoviedb.org/3/'
MOVIE_URL_PART = 'movie/'


def make_tmdb_api_request(method, api_key, extra_params=None):
    extra_params = extra_params or {}
    url = 'https://api.themoviedb.org/3%s' % method
    params = {
        'api_key': api_key,
        'language': 'ru',
    }
    params.update(extra_params)
    return load_json_data_from_url(url, params)

def load_json_data_from_url(base_url, url_params):
    url = '%s?%s' % (base_url, urllib.parse.urlencode(url_params))
    response = urllib.request.urlopen(url).read().decode('utf-8')
    return json.loads(response)


def get_movie(api_key='', movie_id=0):
    """Get json data of movie request by id."""

    params = {
        'api_key': api_key,
        'language': 'ru',
    }
    movie_api_url = urljoin(BASE_API_URL, MOVIE_URL_PART)

    try:
        response = requests.get(
            url=urljoin(movie_api_url, str(movie_id)),
            params=params,
        )
        response.raise_for_status()
    except requests.ConnectionError as conn_error:
        print(f'Connection problems {conn_error}')
    except requests.HTTPError as http_error:
        print(f'Connection problems {http_error}')

    return response.json()


def load_data(path):
    if not os.path.exists(path):
        return None
    with open(path, mode='r', encoding='utf-8') as my_file:
        films_data = json.load(my_file)
        return films_data
