import sys
import os

# Ensure 'src' directory is in sys.path
BASE_DIR = os.path.dirname(__file__)
SRC_DIR = os.path.join(BASE_DIR, "src")
sys.path.insert(0, SRC_DIR)

from decorators.decorators import star_border, emoji_wrap

def format_message(message):
    return message

if __name__ == "__main__":
    # First: star border
    print(star_border(format_message)("Hello from decorators-project!"))
    # Second: emoji wrap
    print(emoji_wrap(format_message)("Hello from decorators-project!"))
