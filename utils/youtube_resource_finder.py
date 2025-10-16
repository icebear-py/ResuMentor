import os
import requests
from dotenv import load_dotenv
load_dotenv()

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
BASE_URL = "https://www.googleapis.com/youtube/v3/search"

def search_youtube_resources(query: str, max_results: int = 2, lang: str = "en"):
    if not YOUTUBE_API_KEY:
        raise ValueError("YOUTUBE_API_KEY not found in environment variables.")

    headers = {"Accept": "application/json"}

    video_params = {
        "key": YOUTUBE_API_KEY,
        "part": "snippet",
        "q": f"{query} tutorial OR course",
        "type": "video",
        "maxResults": max_results,
        "relevanceLanguage": lang,
        "videoDuration": "medium",
        "order": "relevance",
        "safeSearch": "moderate"
    }

    video_res = requests.get(BASE_URL, params=video_params, headers=headers)
    video_data = video_res.json()
    videos = []
    for item in video_data.get("items", []):
        snippet = item["snippet"]
        video_id = item["id"]["videoId"]
        videos.append({
            "title": snippet["title"],
            "channel": snippet["channelTitle"],
            "url": f"https://www.youtube.com/watch?v={video_id}"
        })

    playlist_params = {
        "key": YOUTUBE_API_KEY,
        "part": "snippet",
        "q": f"{query} playlist",
        "type": "playlist",
        "maxResults": max_results,
        "relevanceLanguage": lang,
        "order": "relevance",
        "safeSearch": "moderate"
    }

    playlist_res = requests.get(BASE_URL, params=playlist_params, headers=headers)
    playlist_data = playlist_res.json()
    playlists = []
    for item in playlist_data.get("items", []):
        snippet = item["snippet"]
        playlist_id = item["id"]["playlistId"]
        playlists.append({
            "title": snippet["title"],
            "channel": snippet["channelTitle"],
            "url": f"https://www.youtube.com/playlist?list={playlist_id}"
        })

    return {
        "videos": videos,
        "playlists": playlists
    }

if __name__ == "__main__":
    result = search_youtube_resources("Create AWS account, set up MFA, configure billing alerts")
    print(result)