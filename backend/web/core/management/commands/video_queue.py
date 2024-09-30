from django.core.management import BaseCommand
from core.models import Video, Song, Genre, Category
import requests


class Command(BaseCommand):

    def run_videos(self):
        video_new = Video.objects.filter(slug__icontains="ricktube.ru")
        print("total videos:,", video_new.count())
        for video in video_new:
            url = video.slug
            response = requests.get(url)
            print(f"Response for {url} {response.status_code}")

    def _run_video(self, url: str):
        response = requests.get(url)
        print(f"Response for {url} {response.status_code}")

    def run_categories(self):
        categories = Category.objects.filter(website__icontains="ricktube")
        for cat in categories:
            self._run_video(cat.website)

    def run_genres(self):
        genres = Genre.objects.filter(website__icontains="ricktube")
        for g in genres:
            self._run_video(g.website)

    def run_songs(self):
        songs = Song.objects.filter(youtube_link__icontains="ricktube")
        for s in songs:
            self._run_video(s.youtube_link)

    def handle(self, *args, **options):
        self.run_songs()
        self.run_genres()
        self.run_categories()

