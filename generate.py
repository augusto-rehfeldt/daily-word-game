from ai_generator import generate_word_game
from datetime import date
import re
import os

TODAY = date.today().isoformat()
GAMES_DIR = "games"
GAME_PATH = f"{GAMES_DIR}/{TODAY}.html"
BASE_URL = "https://augusto-rehfeldt.github.io/daily-word-game"

def extract_title(html: str) -> str:
    m = re.search(r"<title>(.*?)</title>", html, re.IGNORECASE | re.DOTALL)
    return m.group(1).strip() if m else "Daily Word Game"

def update_readme(title: str):
    line = f"| {TODAY} | {title} | {BASE_URL}/{GAME_PATH} |\n"

    if not os.path.exists("README.md"):
        with open("README.md", "w", encoding="utf-8") as f:
            f.write(
                "# Daily Word Games\n\n"
                "| Date | Title | Play |\n"
                "|------|-------|------|\n"
            )

    with open("README.md", "r+", encoding="utf-8") as f:
        content = f.read()
        if TODAY in content:
            return  # already added
        f.write(line)

def main():
    html = generate_word_game()
    title = extract_title(html)

    os.makedirs(GAMES_DIR, exist_ok=True)

    with open(GAME_PATH, "w", encoding="utf-8") as f:
        f.write(html)

    # Optional: make index.html always point to latest
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)

    update_readme(title)

if __name__ == "__main__":
    main()
