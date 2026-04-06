from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path

app = FastAPI()

# Locate the folder where this file lives
BASE_DIR = Path(__file__).resolve().parent

# Link the 'static' folder so the browser can download images/sounds
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")

# Link the 'templates' folder for our HTML
templates = Jinja2Templates(directory=BASE_DIR / "templates")

@app.get("/")
async def home(request: Request):
    audio_dir = BASE_DIR / "static" / "audio"
    
    # This automatically finds every .mp3 and creates a button for it!
    animals = [f.stem for f in audio_dir.glob("*.mp3")] if audio_dir.exists() else []
    
    # Use the keyword 'context=' to be safe!
    return templates.TemplateResponse(
        request=request, 
        name="index.html", 
        context={"animals": sorted(animals)}
    )