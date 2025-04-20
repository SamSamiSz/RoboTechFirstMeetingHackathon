"""
Spotify Banger Classifier
-------------------------
• Labels tracks as 1 = banger (popularity >= 70) else 0
• Uses 10 core audio features → Random Forest
• Prints accuracy + asks for your own feature values
"""

import pandas as pd, numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

# ---- 1. Load -----------------------------------------------------------
cols = [
    "popularity","danceability","energy","loudness","speechiness",
    "acousticness","instrumentalness","liveness","valence","tempo"
]
df = pd.read_csv("spotify_tracks.csv", usecols=cols).dropna()

df["banger"] = (df["popularity"] >= 70).astype(int)
X = df.drop(["popularity", "banger"], axis=1)
y = df["banger"]

# ---- 2. Split & pipeline ----------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, stratify=y, random_state=42
)
pipe = make_pipeline(StandardScaler(), RandomForestClassifier(
    n_estimators=200, random_state=42))
pipe.fit(X_train, y_train)

# ---- 3. Evaluate -------------------------------------------------------
pred = pipe.predict(X_test)
print(f"🎧  Accuracy: {accuracy_score(y_test, pred):.2%}")

ConfusionMatrixDisplay.from_predictions(y_test, pred, cmap="Greens")
plt.title("Spotify banger classifier")
plt.show(block=False)

# ---- 4. Live demo ------------------------------------------------------
print("\nEnter song features (danceability energy loudness speechiness acousticness "
      "instrumentalness liveness valence tempo) separated by spaces.")
print("Example: 0.8 0.9 -5.0 0.05 0.02 0.0 0.12 0.6 120")
while True:
    line = input("▶ ")
    if not line.strip():
        break
    try:
        feats = np.array([float(v) for v in line.strip().split()]).reshape(1, -1)
        if feats.shape[1] != X.shape[1]:
            raise ValueError
    except ValueError:
        print("❌  Need", X.shape[1], "numeric values.")
        continue
    print("  ➜  Prediction:", "🔥 BANGER" if pipe.predict(feats)[0] else "💤 Meh")
    
