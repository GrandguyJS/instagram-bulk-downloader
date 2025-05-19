from download_instareels import download_reels
import os
import re
from datetime import datetime

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    output_dir = os.path.join(os.getenv("DOWNLOAD_PATH"), datetime.now().strftime("%d.%m.%Y"))
    files = [file for file in os.listdir(output_dir) if os.path.isfile(os.path.join(output_dir, file)) and file.endswith(".mov")]

    amount = len(files)

    return templates.TemplateResponse(
        request=request, name="index.html", context={"amount": amount}
    )

@app.post("/download")
async def download(reel_url: str = Form(...)):
    download_reels(re.findall(r'https?://\S+', reel_url))
    return RedirectResponse("/", status_code=303)
