import json
import os
import urllib.parse
import urllib.request

import requests
from requests.compat import urljoin


DEFAULT_LANGUAGE = 'ru'

BASE_API_URL = 'https://api.themoviedb.org/3/'
MOVIE_URL_PART = 'movie/'
MOVIE_SEARCH_URL = BASE_API_URL + 'search/movie/'


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


def _make_tmdb_api_request(api_key='', url='', extra_params={}):
    """Base API request."""

    params = {
        'api_key': api_key,
        'language': DEFAULT_LANGUAGE,
    }
    params.update(extra_params)

    try:
        response = requests.get(
            url=url,
            params=params,
        )
        response.raise_for_status()
    except requests.ConnectionError as conn_error:
        print(f'Connection problems {conn_error}')
    except requests.HTTPError as http_error:
        print(f'Connection problems {http_error}')

    return response


def get_movie(api_key='', movie_id=None):
    """Get movie data requested by id and return response object."""

    movie_api_url = urljoin(
        urljoin(BASE_API_URL, MOVIE_URL_PART),
        str(movie_id)
    )

    return _make_tmdb_api_request(
        api_key=api_key,
        url=movie_api_url
    )


def search_movies(api_key='', keyword=''):
    """Search movies by keyword and return response object."""

    extra_params = {
        'query': keyword,
    }

    return _make_tmdb_api_request(
        api_key=api_key,
        url=MOVIE_SEARCH_URL,
        extra_params=extra_params,
    )


def load_data(path):
    if not os.path.exists(path):
        return None
    with open(path, mode='r', encoding='utf-8') as my_file:
        films_data = json.load(my_file)
        return films_data
