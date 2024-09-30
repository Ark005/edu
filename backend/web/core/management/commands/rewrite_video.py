import re

from django.core.management import BaseCommand
from django.db.models import Q

from core.models import Video, Song, Category, Genre, Author


def extract_video_id(link):
    match = re.search(r'/embed/([^?]+)', link)
    return match.group(1) if match else None


def build_proxy_link(video_id) -> str:
    return f"https://ricktube.ru/video?q=https://youtu.be/{video_id}"


def process_record(record, field_name: str):
    youtube_link = getattr(record, field_name, None)
    if not youtube_link:
        return
    video_id = extract_video_id(youtube_link)
    if not video_id:
        return
    new_link = build_proxy_link(video_id)
    print(f"New link for {record.__class__.__name__} {record.id} is {new_link}")
    setattr(record, field_name, new_link)
    record.save()


class Command(BaseCommand):

    def change_videos(self):
        video_new = Video.objects.filter(Q(slug__icontains="youtube") | Q(slug__icontains="edu005.ru"))
        print("total videos:,", video_new.count())
        for video in video_new:
            video_id = extract_video_id(video.slug)
            new_link = build_proxy_link(video_id)
            video.slug = new_link
            video.save()

    def change_genre(self):
        # website
        genres = Genre.objects.filter(website__icontains="youtube")
        print("Genres", genres.count())
        for gen in genres:
            process_record(gen, "website")

    def change_categories(self):
        # website
        categories = Category.objects.filter(website__icontains="youtube")
        print("Categories", categories.count())
        for cat in categories:
            process_record(cat, "website")

    def change_songs(self):
        # youtube_link
        songs = Song.objects.filter(type="youtube")
        print(f"Songs:", songs.count())
        for song in songs:
            if song.youtube_link and "youtube" in song.youtube_link:
                process_record(song, "youtube_link")


    def handle(self, *args, **options):
        self.change_songs()
        self.change_categories()
        self.change_genre()
