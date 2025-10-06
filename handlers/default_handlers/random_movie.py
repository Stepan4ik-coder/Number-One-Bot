import requests
from loader import bot
from telebot.types import Message
from config_data.config import BASE_URL, API_KEY

@bot.message_handler(commands=["random"])
def get_random_movie(message: Message):

    try:
        url = f"{BASE_URL}/v1.4/movie/random"
        headers = {"X-API-KEY": API_KEY}
        response = requests.get(url, headers=headers)
        movie_data = response.json()

        movie_title = movie_data['title']
        movie_year = movie_data['year']
        movie_genre = movie_data['genre']

        bot.send_message(message.chat.id, f"Название фильма: {movie_title}", f"\nГод выпуска: {movie_year}", f"\nЖанр: {movie_genre}")

    except Exception as error:
        bot.send_message(message.chat.id, f"Произошла ошибка: {error}! ")
