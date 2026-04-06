import time
from pathlib import Path
from playsound import playsound  # New, lighter audio library
from PIL import Image

BASE_DIR = Path(__file__).parent

# 1. Collect files
image_extensions = ["*.png", "*.jpg", "*.jpeg"]
image_files = {}

for ext in image_extensions:
    # This finds all files matching the extension and adds them to our dictionary
    for f in BASE_DIR.glob(ext):
        image_files[f.stem.lower()] = f

# 2. Collect audio files (keeping as is

audio_files = {f.stem.lower(): f for f in BASE_DIR.glob("*.mp3")}

all_keys = set(image_files) | set(audio_files)
animals = {
    base: {
        "name": base.capitalize(),
        "audio": audio_files.get(base),
        "image": image_files.get(base)
    }
    for base in all_keys
}
animals["q"] = {"name": "Quit", "audio": None, "image": None}

def find_animal(choice):
    choice = choice.lower().strip()
    if not choice: return None
    if choice in animals: return choice
    for key in animals:
        if key.startswith(choice): return key
    return None

print("--- Toddler Learning App (Playsound Version) ---")

while True:
    print("\nOptions: " + ", ".join([k.upper() for k in animals.keys() if k != 'q']))
    choice = input("\nPress a letter: ").strip()
    key = find_animal(choice)

    if not key:
        print("Try again!")
        continue
    if key == "q":
        break

    info = animals[key]
    
    # 2. Show Image First (so they see it while it talks)
    if info["image"]:
        try:
            Image.open(str(info["image"])).show()
        except Exception as e:
            print(f"Image error: {e}")

    # 3. Play Audio
    if info["audio"]:
        try:
            print(f"Playing sound for {info['name']}...")
            # block=False allows the program to keep running while sound plays
            playsound(str(info["audio"]), block=False)
        except Exception as e:
            print(f"Audio error: {e}")

    time.sleep(1)