# RoboTech First Meeting Mini‑Hackathon

Python projects created for the **RoboTech Society** kick‑off meeting.

## Projects Included

| Folder | Mini‑Game / Mini‑ML | One‑liner |
|--------|---------------------|-----------|
| **EmojiMoodBot/** | *Emoji Mood Bot* | Rule‑based “AI” that labels each chat line as HAPPY, SAD, or NEUTRAL. |
| **HangmanLite/** | *Hangman Lite* | Fast console word‑guessing game with ASCII stick‑figure suspense. |
| **Spotify_ML_Project/** | *Spotify Banger Classifier* | Tiny Random‑Forest model that predicts if a track is a 🔥 BANGER (popularity ≥ 70) or 💤 Meh using audio features. |

---

## Quick Start

```bash
# clone the repo (or download as ZIP)
$ git clone https://github.com/SamSamiSz/RoboTechFirstMeetingHackathon.git
$ cd RoboTechFirstMeetingHackathon

# -------------------
# 1) Emoji Mood Bot
# -------------------
$ python EmojiMoodBot/emoji_mood_bot.py

# -------------------
# 2) Hangman Lite
# -------------------
$ python HangmanLite/hangman_lite.py

# -----------------------------
# 3) Spotify Banger Classifier
# -----------------------------
$ cd Spotify_ML_Project
# first‑time: install light deps
$ pip install pandas scikit-learn matplotlib
$ python Spotify_Predictor.py   # pops accuracy + interactive prompt
```

**Requirements**
* Emoji & Hangman: Python ≥ 3.8 (standard library only)
* Spotify ML: `pandas`, `scikit‑learn`, `matplotlib`  
  *(install via `pip install -r requirements.txt` or the one‑liner above)*

---

## Folder Layout

```
RoboTechFirstMeetingHackathon/
├─ EmojiMoodBot/
│  └─ emoji_mood_bot.py
├─ HangmanLite/
│  └─ hangman_lite.py
├─ Spotify_ML_Project/
│  ├─ Spotify_Predictor.py
│  └─ spotify_tracks.csv   # 9 MB sample of Kaggle dataset
└─ README.md
```

---

## How to Play / Test

### Emoji Mood Bot
1. Launch the script.  
2. Type any sentence and press **Enter**.  
3. The bot replies with 🙂 HAPPY, 🙁 SAD, or 😐 NEUTRAL.  Blank line exits.

### Hangman Lite
1. Launch the script.  
2. Guess one letter per turn until you reveal the word or exhaust six misses.  
3. Enjoy the retro ASCII hangman drawing!

### Spotify Banger Classifier
1. Make sure `spotify_tracks.csv` is present (9 MB sample included).  
2. Run the script; it trains in ≈5 s and shows test accuracy (~90 %).  
3. At the prompt, paste nine numeric audio‑feature values (see Tunebat / Spotify API) to see if the model shouts **🔥 BANGER** or **💤 Meh**.

---

*Built by **Sami** — Vice President, RoboTech Society @ DePaul University — for the 2025 first‑meeting mini‑hackathon.*

