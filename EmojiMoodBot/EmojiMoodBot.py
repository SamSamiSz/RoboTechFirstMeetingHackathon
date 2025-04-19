# emoji_mood_bot.py
import re
from random import choice

HAPPY = {"happy", "love", "great", "yay", "awesome", "😊", "😀"}
SAD   = {"sad", "hate", "bad", "ugh", "terrible", "😢", "😔"}

def classify(text: str) -> str:
    words = set(re.findall(r"\w+|[^\w\s]", text.lower()))
    happy_hits = len(words & HAPPY)
    sad_hits   = len(words & SAD)
    if happy_hits > sad_hits:
        return "🙂 HAPPY"
    if sad_hits > happy_hits:
        return "🙁 SAD"
    return "😐 NEUTRAL"

TIPS = [
    "Keep going—you’re doing great!",
    "Robots believe in you 🤖✨",
    "Take a sip of water, champ."
]

print("Tiny Emoji Mood Bot (blank line to quit)")
while True:
    user = input("You: ")
    if not user.strip():
        break
    mood = classify(user)
    print("Bot:", mood)
    if "🙁" in mood:
        print("Bot:", choice(TIPS))
print("Bye! 👋")
