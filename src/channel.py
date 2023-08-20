import requests
import json
import os

API_KEY: str = os.getenv('YT_API_KEY')


class Channel:
    """Класс для ютуб-канала"""
    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.url = f"https://www.googleapis.com/youtube/v3/channels?id={channel_id}&key={API_KEY}" \
                   f"&part=snippet,contentDetails,statistics,status"
        self.response = requests.request('GET', url=self.url)

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(self.response.text)