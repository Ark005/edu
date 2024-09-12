import re

from django.core.management import BaseCommand
from django.db.models import Q

from core.models import Video


def extract_video_id(link):
    match = re.search(r'/embed/([^?]+)', link)
    return match.group(1) if match else None


def build_proxy_link(video_id) -> str:
    return f"https://ricktube.ru/video?q=https://youtu.be/{video_id}"


class Command(BaseCommand):
    def handle(self, *args, **options):
        video_new = Video.objects.filter(Q(slug__icontains="youtube") | Q(slug__icontains="edu005.ru"))
        print("total videos:,", video_new.count())
        for video in video_new:
            video_id = extract_video_id(video.slug)
            new_link = build_proxy_link(video_id)
            video.slug = new_link
            video.save()
