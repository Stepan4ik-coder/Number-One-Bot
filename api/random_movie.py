import requests


BASE_URL = 'https://api.kinopoisk.dev/'
API_KEY = '8217471619:AAHV75CPNFuTj2YCEmKF44qE2-8-dwJlJ5U'

def get_random_movie():
    url = f"{BASE_URL}/v1.4/movie/random"
    headers = {"X-API-KEY": API_KEY}

    response = requests.get(url, headers=headers)
    return response.json()

if __name__ == '__main__':
    movie = get_random_movie()
    print(movie)