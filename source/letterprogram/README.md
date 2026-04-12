# 🌟 Toddler Learning Adventure

An interactive Python web application that teaches toddlers letters and animal names through bright visuals, playful sounds, and instant feedback.

## ✨ New Feature: Media-Driven Letter Cards

This release introduces an automatic media discovery engine for the learning experience:
- Auto-detects all `.mp3` files in `app/static/audio/`
- Builds one learning card per animal name
- Displays the animal image if a matching `.jpg` or `.png` file exists
- Plays the animal sound on tap/click for fast reinforcement

## 🚀 What’s Included

- **Smart media discovery**: no hard-coded animal list required
- **Dynamic letter cards**: first letter hero, animated card hover states, and touch-friendly design
- **Responsive UI**: works smoothly on desktops, tablets, and phones
- **FastAPI backend**: lightweight Python web service with Jinja2 templating
- **Docker-ready**: easily deploy as a container

## 🧩 Tech Stack

- **Python**: 3.14+
- **FastAPI**: backend web framework
- **Jinja2**: server-side templates
- **Uvicorn**: ASGI server
- **Pillow**: image support
- **playsound**: browser-triggered audio playback for desktop

## 📦 Installation

### Prerequisites
- Python 3.14 or higher
- `uv` package manager: `pip install uv`

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/ShivGitLabbing/my-automation-project.git
   cd source/letterprogram
   ```

2. Install dependencies:
   ```bash
   uv sync
   ```

## ▶️ Run Locally

1. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

2. Start the app:
   ```bash
   uv run uvicorn app.main:app --reload
   ```

3. Open `http://127.0.0.1:8000` in your browser.

## 🐾 Add Your Own Animals

To add new cards:
- Add sound files to `app/static/audio/` using animal names, e.g. `lion.mp3`
- Add matching images to `app/static/images/` using the same base name, e.g. `lion.jpg`
- The interface updates automatically when the server restarts

## 🐳 Docker Deployment

Build the image:
```bash
docker build -t toddler-app .
```

Run it:
```bash
docker run -p 8000:8000 toddler-app
```

Then visit `http://localhost:8000`.

## 📁 Project Structure

```
letterprogram/
├── app/
│   ├── main.py
│   ├── static/
│   │   ├── audio/
│   │   └── images/
│   └── templates/
│       └── index.html
├── Dockerfile
├── README.md
├── pyproject.toml
├── __init__.py
└── .dockerignore
```

## 🔍 How It Works

1. The backend reads `app/static/audio/` for `.mp3` files.
2. It builds a card for every audio file found.
3. Each card shows:
   - the first letter of the animal name
   - the animal image if available
   - a tap-to-play sound button

## 🛠️ Notes

- Missing images are handled gracefully by the UI.
- New media files are automatically included without changing code.

## 🤝 Contribution Guide

1. Fork the repo
2. Create a new branch: `git checkout -b feature/letterprogram-readme`
3. Make your changes
4. Commit: `git commit -am 'feat: improve README and Docker support for letterprogram'`
5. Push: `git push origin feature/letterprogram-readme`
6. Open a pull request

## 📄 License

This project is licensed under the MIT License.
