reels_text = """Day 2
https://www.instagram.com/reel/DJVUrydvNot/?igsh=em1rNHVrODJsZnFn
"""

# Download all links    
import re
import os
import yt_dlp
from datetime import datetime

from dotenv import load_dotenv
load_dotenv(os.path.join(os.path.dirname(__file__), "secret.env"))

output_dir = os.path.join(os.getenv("DOWNLOAD_PATH"), datetime.now().strftime("%d.%m.%Y"))
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def download_reels(links): # Downloads all reels as .mov files
    for i, link in enumerate(links, start=1):
        ydl_opts = {
            "outtmpl": f"{output_dir}/%(id)s.%(ext)s",
            "format": "bestvideo+bestaudio/best",
            "postprocessors": [{
                "key": "FFmpegVideoConvertor",
                "preferedformat": "mov"
            }],
            "quiet": True,
            "cookiefile": "cookies.txt"
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])
                print("Downloaded Video #", i)
        except Exception as e:
            print(e)

if __name__ == "__main__":
    download_reels(re.findall(r'https?://\S+', reels_text))