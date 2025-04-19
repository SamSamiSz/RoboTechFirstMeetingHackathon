# hangman_lite.py
import random
WORDS = ["robot", "python", "gear", "sensor", "matrix", "drone"]

HANGMAN = [
    "",          # 6 tries left
    " O ",       # 5
    " O\n | ",   # 4
    " O\n/| ",   # 3
    " O\n/|\\",  # 2
    " O\n/|\\\n/  ",  # 1
    " O\n/|\\\n/ \\", # 0 – game over
]

secret = random.choice(WORDS)
discovered = ["_"] * len(secret)
guessed = set()
tries = 6

print("Welcome to Hangman Lite! Type one letter per turn.\n")

while tries and "_" in discovered:
    print("\nWord:", " ".join(discovered))
    print("Misses left:", tries)
    guess = input("Your guess: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue
    if guess in guessed:
        print("Already tried that one!")
        continue

    guessed.add(guess)
    if guess in secret:
        for i, ch in enumerate(secret):
            if ch == guess:
                discovered[i] = guess
        print("Nice!")
    else:
        tries -= 1
        print("Nope!")
        print(HANGMAN[6 - tries])

# End‑game message
if "_" not in discovered:
    print("\n🎉  You won! The word was:", secret)
else:
    print("\n💀  Out of tries! The word was:", secret)
