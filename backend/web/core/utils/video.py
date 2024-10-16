import re
from typing import Optional


def extract_video_id(link):
    match = re.search(r'/embed/([^?]+)', link)
    return match.group(1) if match else None


def build_youtube_preview(video_id: str) -> str:
    return f"https://img.youtube.com/vi/{video_id}/0.jpg"


def get_video_preview_link(link: str) -> Optional[str]:
    if "ricktube" in link:
        video_id = link.split("/")[-1]
    else:
        video_id = extract_video_id(link)
    return build_youtube_preview(video_id)



