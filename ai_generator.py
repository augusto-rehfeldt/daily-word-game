import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

SYSTEM_PROMPT = """
You generate a single, self-contained daily word game.

Hard requirements:
- Output MUST be a complete, valid HTML document.
- Inline CSS and vanilla JavaScript only.
- Fully playable in the browser (input, feedback, clear win condition).
- No external assets, fonts, images, or libraries.
- English only.

Design constraints:
- The entire game must fit within a 1080p screen height (no scrolling).
- Use compact layout, limited text, and restrained spacing.
- Assume desktop viewport ~1200x800 minimum.

Content constraints:
- The game must be new and original each time.
- Do NOT reuse common formats verbatim (no Wordle clones, no ladders, no anagrams-only).
- Clear, concise rules shown on the page.
- Single game only.

Quality bar:
- The game should feel intentional, not a demo.
- Minimal but polished UI.
- Deterministic gameplay (no timers, no network, no randomness requiring reloads).
"""


def generate_word_game():
    response = client.responses.create(
        model="gpt-5",
        input=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": "Create today's daily word game."}
        ],
    )

    return response.output_text.strip()
