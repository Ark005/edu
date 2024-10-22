import re
from typing import Optional


def extract_video_id(link):
    match = re.search(r'/embed/([^?]+)', link)
    return match.group(1) if match else None


def build_youtube_preview(video_id: str) -> str:
    return f"https://img.youtube.com/vi/{video_id}/0.jpg"


def get_video_id(link: str) -> str:
    if "ricktube" in link:
        return link.split("/")[-1]
    return extract_video_id(link)


def get_video_preview_link(link: str) -> Optional[str]:
    return build_youtube_preview(get_video_id(link))



