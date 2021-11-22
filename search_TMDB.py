import os
import sys

from dotenv import load_dotenv

from utils import get_movie, get_recommendations, print_movies, search_movies

load_dotenv()


def main():
    user_api_key = os.getenv('TMDB_API_KEY')

    if not user_api_key:
        print('No API Key! Please check env variable TMDB_API_KEY!')
        raise sys.exit(0)

    while True:
        print(
            """Choose option:
               1) search movies
               2) get recommendations
               3) get movie by id
               Or x for exit."""
        )
        option = input('> ')
        resp = None
        if option == '1':
            keyword = input('Enter keyword for search: ')
            resp = search_movies(
                api_key=user_api_key,
                keyword=keyword,
            )

        if option == '2':
            movie_id = input('Enter movie id for search recommendations: ')
            resp = get_recommendations(
                api_key=user_api_key,
                movie_id=movie_id,
            )
        if option == '3':
            movie_id = input('Enter movie id for detais: ')
            resp = get_movie(
                api_key=user_api_key,
                movie_id=movie_id,
            )
        if option in ('x', 'X'):
            sys.exit(1)

        json_data = resp.json()
        if resp.status_code in [401, 404]:
            print(f'{json_data["status_message"]}')
            continue

        if 'results' in json_data:
            movies = json_data['results']
            print_movies(movies)
        else:
            print((
                f'Requested movie founded: {json_data["title"]},'
                f' budget: {json_data["budget"]}'
            ))

        input('Press anykey to proceed.')


if __name__ == '__main__':
    main()
