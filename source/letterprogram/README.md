# 👶 Toddler Learning App

A fun, interactive Python application designed to help toddlers learn letters and animal names through visual and auditory feedback.

## 🚀 Features

- **Letter Recognition**: Supports single-letter inputs or full animal names.
- **Dynamic Media Detection**: Automatically scans the directory for .png, .jpg, and .mp3 files. No hard-coding required!
- **Visual & Audio Feedback**: Displays an image of the animal while playing its corresponding sound effect.
- **Modern Python Stack**: Built using uv for lightning-fast dependency management and Python 3.14.
- **Web-Based Interface**: Interactive web app built with FastAPI and Jinja2 templates.
- **Responsive Design**: Colorful, engaging UI optimized for touch interaction.

## 🛠️ Tech Stack

- **Language**: Python 3.14+
- **Framework**: FastAPI
- **Package Manager**: uv
- **Libraries**:
  - Pillow (Image processing)
  - playsound (Cross-platform audio playback)
  - pathlib (Object-oriented filesystem paths)
  - Jinja2 (Templating)
  - Uvicorn (ASGI server)

## 📦 Installation

### Prerequisites
- Python 3.14 or higher
- uv package manager (install via `pip install uv`)

### Setup
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd letterprogram
   ```

2. Install dependencies using uv:
   ```bash
   uv sync
   ```

## 🚀 Usage

### Running Locally
1. Activate the virtual environment:
   ```bash
   uv run python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. Run the application:
   ```bash
   uv run uvicorn app.main:app --reload
   ```

3. Open your browser and navigate to `http://127.0.0.1:8000`

### Adding Media Files
- Place animal images (`.jpg`, `.png`) in `app/static/images/`
- Place animal sounds (`.mp3`) in `app/static/audio/`
- The app automatically detects and creates interactive cards for each animal

## 🐳 Docker Deployment

### Building the Image
```bash
docker build -t toddler-app .
```

### Running the Container
```bash
docker run -p 8000:8000 toddler-app
```

Access the app at `http://localhost:8000`

## 📁 Project Structure

```
letterprogram/
├── app/
│   ├── main.py              # FastAPI application
│   ├── static/
│   │   ├── audio/           # Animal sound files (.mp3)
│   │   └── images/          # Animal images (.jpg, .png)
│   └── templates/
│       └── index.html       # Main web interface
├── Dockerfile               # Docker configuration
├── pyproject.toml           # Project dependencies and metadata
├── README.md                # This file
└── __init__.py              # Python package marker
```

## 🎯 How It Works

1. The app scans the `static/audio/` directory for `.mp3` files
2. For each audio file, it creates an interactive card displaying:
   - The first letter of the animal name (capitalized)
   - The corresponding image from `static/images/`
   - Plays the sound when the card is clicked
3. The web interface uses responsive CSS for a touch-friendly experience

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and test thoroughly
4. Commit your changes: `git commit -am 'Add new feature'`
5. Push to the branch: `git push origin feature-name`
6. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Built with ❤️ for educational purposes
- Inspired by the joy of learning through play
