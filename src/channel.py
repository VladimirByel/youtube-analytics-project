import requests
import json
import os
from googleapiclient.discovery import build

API_KEY: str = os.getenv('YT_API_KEY')


class Channel:
    """Класс для ютуб канала"""


    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала."""
        self.channel_id = channel_id
        youtube = build('youtube', 'v3', developerKey=API_KEY)
        self.channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()


    def printj(self) -> None:
        """Выводит словарь в json-подобном удобном формате с отступами"""
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))


    #def print_info(self) -> None:
    #    """Выводит в консоль информацию о канале."""
    #    print(self.response.text)