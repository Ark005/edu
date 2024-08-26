from django.core.management import BaseCommand
from core.models import Video


class Command(BaseCommand):

    def handle(self, *args, **options):
        video_new = Video.objects.filter(slug__icontains='youtube')
        print("total videos:,", video_new.count())
        possible_versions = [
            'www.youtube.com',
            'youtube.com',
        ]
        for video in video_new:
            for version in possible_versions:
                if version in video.slug:
                    slug = video.slug
                    video.slug = video.slug.replace(version, 'edu005.ru')
                    video.save()
                    print(f"{slug} replaced for {video.slug}")
