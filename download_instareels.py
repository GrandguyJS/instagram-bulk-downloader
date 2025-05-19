reels_text = """  """

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
    ydl_opts = {
        "outtmpl": f"{output_dir}/%(id)s1.%(ext)s",
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
            ydl.download(links)
    except Exception as e:
        print(e)
    for link in links:
        if not os.path.exists(os.path.join(output_dir, link.split("/reel/")[1].split("/")[0]+".mov")):
            with open(os.path.join(os.path.dirname(__file__), "failed.txt"), "a") as f:
                f.write(link + "\n")

if __name__ == "__main__":
    download_reels(re.findall(r'https?://\S+', reels_text))