import json
from googleapiclient.discovery import build
import os


class Channel:
    """Класс для ютуб канала"""

    API_KEY = os.getenv('YT_API_KEY')

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала."""
        self.__channel_id = channel_id
        youtube = build('youtube', 'v3', developerKey=Channel.API_KEY)
        self.channel = youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        self.description = self.channel['items'][0]['snippet']['description']
        self.title = self.channel['items'][0]['snippet']['title']
        self.url = f"www.youtube.com/channel/{self.__channel_id}"
        self.number_of_subscribers = self.channel['items'][0]['statistics']['subscriberCount']
        self.video_count = self.channel['items'][0]['statistics']['videoCount']
        self.number_of_views = self.channel['items'][0]['statistics']['viewCount']

    @property
    def channel_id(self):
        return self.__channel_id

    #def printj(self) -> None:
    #    """Выводит словарь в json-подобном удобном формате с отступами"""
    #    print(json.dumps(self.channel, indent=2, ensure_ascii=False))

    @staticmethod
    def get_service():
        return build('youtube', 'v3', developerKey=Channel.API_KEY)

    def to_json(self, name):
        json_to_be = {
            'id': {self.__channel_id},
            'title': {self.title},
            'description': {self.description},
            'link': {self.url},
            'subscribers': {self.number_of_subscribers},
            'number of videos': {self.video_count},
            'number of views': {self.number_of_views}
        }
        txt = str(json_to_be)
        jsoned_dict = json.dumps(txt)
        with open(name, 'a') as file:
            file.write(jsoned_dict)
            #json.dumps(json_to_be, file, indent=2, ensure_ascii=False)

