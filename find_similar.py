import os
import sys
from datetime import datetime

from dotenv import load_dotenv

from utils import get_recommendations

load_dotenv()


def main():
    user_api_key = os.getenv('TMDB_API_KEY')

    if not user_api_key:
        print('No API Key! Please check env variable TMDB_API_KEY!')
        raise sys.exit(0)

    movie_id = input('Enter movie id for search recommendations: ')

    recomm_resp = get_recommendations(
        api_key=user_api_key,
        movie_id=movie_id,
    )

    movies = recomm_resp.json()['results']

    if recomm_resp.status_code in [401, 404]:
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
