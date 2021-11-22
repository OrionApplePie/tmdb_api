import os
import sys

from dotenv import load_dotenv

from utils import get_movie

load_dotenv()

TEST_MOVIE_NUMBER = 215


def main():
    user_api_key = os.getenv('TMDB_API_KEY')

    if not user_api_key:
        print('No API Key! Please check env variable TMDB_API_KEY!')
        raise sys.exit(0)

    test_movie_resp = get_movie(
        api_key=user_api_key,
        movie_id=TEST_MOVIE_NUMBER
    )

    if 'success' in test_movie_resp:
        print(f'{test_movie_resp["status_message"]}')
        sys.exit(0)

    print('API Key is valid and TMDB is up.')
    print()
    print(
        (f'Requested movie finded: {test_movie_resp["title"]},'
         f' budget: {test_movie_resp["budget"]}')
    )


if __name__ == '__main__':
    main()
