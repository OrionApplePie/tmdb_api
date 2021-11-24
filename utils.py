from datetime import datetime

import requests
from requests.compat import urljoin


DEFAULT_LANGUAGE = 'ru'

BASE_API_URL = 'https://api.themoviedb.org/3/'
MOVIE_URL_PART = 'movie/'
MOVIE_SEARCH_URL = BASE_API_URL + 'search/movie/'


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


def get_movie(api_key='', movie_id=None, recomm=False):
    """Get movie data requested by id and return response object."""

    movie_api_url = urljoin(
        urljoin(BASE_API_URL, MOVIE_URL_PART),
        str(movie_id)
    )
    extra_params = {
            'append_to_response': 'recommendations',
    } if recomm else {}

    return _make_tmdb_api_request(
        api_key=api_key,
        url=movie_api_url,
        extra_params=extra_params,
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


def print_movies(movies=None):
    """Print list of movies from dict."""
    if movies is None:
        print('No movies...')
        return None

    for movie in movies:
        if movie['release_date']:
            year = datetime.strptime(movie['release_date'], '%Y-%m-%d').year
        else:
            year = 'N/A'  #TODO: Add checking other fields, sort by popularity

        print(f'id={movie["id"]} - {movie["title"]} ({year}), popularity: {movie["popularity"]}')
