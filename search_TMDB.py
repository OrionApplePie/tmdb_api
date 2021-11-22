import os
import sys
from datetime import datetime

from dotenv import load_dotenv

from utils import search_movies

load_dotenv()


def main():
    user_api_key = os.getenv('TMDB_API_KEY')

    if not user_api_key:
        print('No API Key! Please check env variable TMDB_API_KEY!')
        raise sys.exit(0)

    keyword = input('Enter keyword for search: ')

    movies_resp = search_movies(
        api_key=user_api_key,
        keyword=keyword,
    )

    movies = movies_resp.json()['results']

    if movies_resp.status_code in [401, 404]:
        print(f'{movies["status_message"]}')
        sys.exit(0)

    for movie in movies:
        if movie['release_date']:
            year = datetime.strptime(movie['release_date'], '%Y-%m-%d').year
        else:
            year = 'N/A'  #TODO: Add checking other fields

        print(f'{movie["title"]} ({year}), popularity: {movie["popularity"]}')


if __name__ == '__main__':
    main()
