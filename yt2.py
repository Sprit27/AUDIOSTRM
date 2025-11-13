import yt_dlp
import vlc


murl = input("Enter YouTube Playlist/Video URL: ")

class SilentLogger:
    def debug(self, msg): pass
    def warning(self, msg): pass
    def error(self, msg): print(msg)

def get_playlist_audio_urls(playlist_url):
    ydl_opts = {
        'quiet': True,
        'extract_flat': False,
        'no_warnings': True,
        'logger': SilentLogger(),
        'format': 'bestaudio/best',
        'cookiefile': 'cookies.txt',
    }
    titles = []
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(playlist_url, download=False)
        if "entries" in info:  # it's a playlist
            for entry in info["entries"]:
                try:
                    if entry:
                        titles.append((entry.get("title")))
                except Exception as e:
                    print(f"Skipping a video due to error: {e}")
        else:
            titles.append((info.get("title")))  # single video fallback
    return titles

print(get_playlist_audio_urls(murl))