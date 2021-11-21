import os

from dotenv import load_dotenv

from utils import is_valid_api_key

load_dotenv()

TEST_MOVIE_NUMBER = 215


def main():
    user_api_key = os.getenv('TMDB_API_KEY')

    if not user_api_key:
        print('No API Key! Please check env variable TMDB_API_KEY!')
        raise SystemExit

    if is_valid_api_key(
        api_key=user_api_key,
        film_id=TEST_MOVIE_NUMBER
    ):
        print('API Key is valid and TMDB is up.')

    else:
        print('Invalid API Key!')


if __name__ == '__main__':
    main()
