import json
import os
import urllib.request
import urllib.parse

from dotenv import load_dotenv

from utils import make_tmdb_api_request


load_dotenv()

def load_films(user_api_key, films_amount=1000):
    all_films = []
    for film_id in range(films_amount):
        try:
            all_films.append(make_tmdb_api_request(method='/movie/%d' % film_id, api_key=user_api_key))
        except urllib.error.HTTPError as err:
            if err.code == 404:  #if no film on this id
                continue
            else:
                raise
        finally:
            print('%s percent complete' % str(film_id*100/ films_amount))
    return all_films


if __name__ == '__main__':
    user_api_key = os.getenv('TMDB_API_KEY')

    if not user_api_key:
        print('No API Key! Please check env variable TMDB_API_KEY!')
        raise SystemExit
    films_amount = 1000
    print('please, wait, this operation may take smth like 15-20 minutes')
    all_films = load_films(user_api_key, films_amount)

    with open(file='MyFilmDB.json', mode='w', encoding='utf-8') as my_file:
        json.dump(all_films, my_file)
