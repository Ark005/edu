from django.core.management import BaseCommand
from core.models import Video
import requests


class Command(BaseCommand):
    def handle(self, *args, **options):
        video_new = Video.objects.filter(slug__icontains="ricktube.ru")
        print("total videos:,", video_new.count())
        for video in video_new:
            url = video.slug
            response = requests.get(url)
            print(f"Response for {url} {response.status_code}")
