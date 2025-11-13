import yt_dlp
import vlc
import time

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
    urls = []
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(playlist_url, download=False)
        if "entries" in info:  # it's a playlist
            for entry in info["entries"]:
                try:
                    if entry:
                        urls.append((entry.get("title"), entry["url"]))
                except Exception as e:
                    print(f"Skipping a video due to error: {e}")
        else:
            urls.append((info.get("title"), info["url"]))  # single video fallback
    return urls

def play_audio_stream(urls):
    player = vlc.MediaPlayer()
    for title, url in urls:
        print(f"\n▶ Now Playing: {title}\n")
        player.set_mrl(url)
        player.play()
        time.sleep(1)
        while player.is_playing():
            time.sleep(0.5)
    print("\n✅ Playlist finished.")

# Run
playlist = get_playlist_audio_urls(murl)
if playlist:
    play_audio_stream(playlist)
else:
    print("❌ Could not fetch playlist or it’s empty.")
