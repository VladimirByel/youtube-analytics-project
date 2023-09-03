import isodate
from googleapiclient.discovery import build
import googleapiclient
from src.video import API_KEY, API_VERSION, API_SERVICE_NAME, Video
from datetime import timedelta


class PlayList:

    def __init__(self, url):
        youtube = googleapiclient.discovery.build(
            API_SERVICE_NAME, API_VERSION, developerKey=API_KEY)

        request = youtube.playlistItems().list(
            playlistId=url,
            part="contentDetails",
            maxResults=50
        ).execute()
        self.__request_ = youtube.playlists().list(
            id=url,
            part="snippet",
            maxResults=50
        ).execute()
        self.title = self.__request_["items"][0]["snippet"]["title"]
        self.url = f"https://www.youtube.com/playlist?list={url}"

        self.__video_ids: list[str] = [video['contentDetails']['videoId'] for video in request['items']]
        self.__interval = timedelta()

    def total_duration(self):
        duration = []
        for video in self.__video_ids:
            example = Video(video)
            for i in example.request.execute()['items']:
                # YouTube video duration is in ISO 8601 format
                iso_8601_duration = i['contentDetails']['duration']
                duration.append(isodate.parse_duration(iso_8601_duration))
        for time in duration:
            self.__interval += time
        return self.__interval

    def show_best_video(self):
        result = ""
        number = 0
        for video in self.__video_ids:
            example = Video(video)
            if int(example.request.execute()['items'][0]['statistics']['likeCount']) > number:
                result = f"https://youtu.be/{example.request.execute()['items'][0]['id']}"
                number = int(example.request.execute()['items'][0]['statistics']['likeCount'])
        return result

    def __str__(self):
        return self.__interval

    @staticmethod
    def total_seconds(value: timedelta):
        return value.total_seconds()


