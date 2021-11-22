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


def get_recommendations(api_key='', movie_id=''):
    """Get recommended movies by movie."""

    movie_api_url = urljoin(
        urljoin(BASE_API_URL, MOVIE_URL_PART),
        str(movie_id)
    )

    recomm_url = urljoin(
        movie_api_url,
        f'{movie_id}/recommendations'
    )

    return _make_tmdb_api_request(
        api_key=api_key,
        url=recomm_url,
    )
