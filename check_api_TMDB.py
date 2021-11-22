import os
import sys
from datetime import datetime

from dotenv import load_dotenv

from utils import get_movie, search_movies

load_dotenv()

TEST_MOVIE_NUMBER = 215
TEST_SERACH_STRING = 'Мqwqwqw'


def main():
    user_api_key = os.getenv('TMDB_API_KEY')

    if not user_api_key:
        print('No API Key! Please check env variable TMDB_API_KEY!')
        raise sys.exit(0)

    test_movie_resp = get_movie(
        api_key=user_api_key,
        movie_id=TEST_MOVIE_NUMBER
    )
    test_movie_json = test_movie_resp.json()

    if test_movie_resp.status_code in [401, 404]:
        print(f'{test_movie_json["status_message"]}')
        sys.exit(0)

    print('API Key is valid and TMDB is up.')
    print()
    print((
        f'Requested movie founded: {test_movie_json["title"]},'
        f' budget: {test_movie_json["budget"]}'
    ))

    movies_resp = search_movies(
        api_key=user_api_key,
        keyword=TEST_SERACH_STRING,
    )

    movies = movies_resp.json()['results']

    if movies_resp.status_code in [401, 404]:
        print(f'{movies["status_message"]}')
        sys.exit(0)

    for movie in movies:
        year = datetime.strptime(movie['release_date'], '%Y-%m-%d').year

        print(f'{movie["title"]} ({year}), popularity: {movie["popularity"]}')


if __name__ == '__main__':
    main()
