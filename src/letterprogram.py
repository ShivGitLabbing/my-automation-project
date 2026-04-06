# This Program is able to produce sound effect or generate images depending on the user letter input and is targetted to toddlers learning to read write and talk.

from pathlib import Path
import sound
from PIL import Image
import time

BASE_DIR = Path(__file__).parent

# Collect files (case-insensitive keys)
image_files = {f.stem.lower(): f for f in BASE_DIR.glob("*.png")}
audio_files = {f.stem.lower(): f for f in BASE_DIR.glob("*.mp3")}

# Build animals dictionary with all keys from both sets
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
    if choice in animals:
        return choice
    for key in animals:
        if key.startswith(choice):
            return key
    return None

# Main loop
while True:
    print("\nAvailable animals:")
    for k, v in animals.items():
        if k == "q":
            print(f"{k} - {v['name']}")
        else:
            img = "Yes" if v["image"] else "No"
            aud = "Yes" if v["audio"] else "No"
            print(f"{k} - {v['name']} (Image: {img}, Audio: {aud})")

    choice = input("\nChoose animal (letter or name, q to quit): ").strip()
    key = find_animal(choice)

    if not key:
        print("Invalid choice, try again.")
        continue
    if key == "q":
        print("Goodbye!")
        break

    info = animals[key]

    # Play audio if available
    if info["audio"]:
        try:
            player = sound.AudioPlayer(str(info["audio"]))
            player.play()
            time.sleep(10)          # ← 10 seconds playback time
        except Exception as e:
            print(f"Audio error: {e}")
    else:
        print(f"No audio for {info['name']}")

    # Show image if available
    if info["image"]:
        try:
            Image.open(str(info["image"])).show()
        except Exception as e:
            print(f"Image error: {e}")
    else:
        print(f"No image for {info['name']}")


