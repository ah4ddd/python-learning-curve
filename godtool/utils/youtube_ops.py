import yt_dlp

def download_video(url, path='.'):
    # Clean the URL by removing escape characters
    clean_url = url.replace('\\', '')

    ydl_opts = {
        'outtmpl': f'{path}/%(title)s.%(ext)s',
        'format': 'best'
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading video...")
            ydl.download([clean_url])
        print(f"Downloaded to {path}")
    except Exception as e:
        print(f"Error downloading video: {e}")
        raise
