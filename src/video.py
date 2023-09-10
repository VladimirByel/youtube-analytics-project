import os
import googleapiclient
import googleapiclient.discovery

API_KEY = os.getenv('YT_API_KEY')
API_SERVICE_NAME = "youtube"
API_VERSION = "v3"


class Video:

    def __init__(self, video_id):
        self.id = video_id
        youtube = googleapiclient.discovery.build(API_SERVICE_NAME, API_VERSION, developerKey=API_KEY)
        # Get credentials and create an API client
        self.request = youtube.videos().list(
            part="snippet,statistics,contentDetails,topicDetails",
            id=self.id,
            maxResults=50
        )
        video_response = self.request.execute()
        try:
            self.video_title: str = video_response['items'][0]['snippet']['title']
        except IndexError:
            self.video_title = None
            self.comment_count = None
            self.like_count = None
            self.view_count = None
        else:
            self.video_title: str = video_response['items'][0]['snippet']['title']
            self.view_count: int = video_response['items'][0]['statistics']['viewCount']
            self.like_count: int = video_response['items'][0]['statistics']['likeCount']
            self.comment_count: int = video_response['items'][0]['statistics']['commentCount']

    def __str__(self):
        return f'{self.video_title}'


class PLVideo(Video):

    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id
