import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file into a list of dictionaries."""
    songs = []  # We will fill this list with one dictionary per song.

    # Open the file for reading. newline="" is what the csv module recommends,
    # and "with" closes the file automatically when we're done.
    with open(csv_path, newline="", encoding="utf-8") as file:
        # DictReader reads the header row (id,title,artist,...) and gives us
        # each following row as a dictionary like {"id": "1", "title": "..."}.
        # Every value starts out as a string, so we convert the numbers below.
        reader = csv.DictReader(file)

        for row in reader:
            song = {
                # Whole numbers -> int
                "id": int(row["id"]),
                "tempo_bpm": int(row["tempo_bpm"]),
                # Decimal numbers -> float
                "energy": float(row["energy"]),
                "valence": float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
                # Text fields stay as strings
                "title": row["title"],
                "artist": row["artist"],
                "genre": row["genre"],
                "mood": row["mood"],
            }
            songs.append(song)

    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score one song against user preferences, returning (score, reasons)."""
    score = 0.0          # running total of points
    reasons = []         # human-readable list explaining each award

    # 1. Genre match: worth 2.0 points (the strongest signal).
    #    .get() returns None instead of crashing if the key is missing.
    if song["genre"] == user_prefs.get("genre"):
        score += 1.0
        reasons.append("genre match (+1.0)")

    # 2. Mood match: worth 1.0 point.
    if song["mood"] == user_prefs.get("mood"):
        score += 1.0
        reasons.append("mood match (+1.0)")

    # 3. Energy similarity: up to 1.0 point.
    #    The closer the song's energy is to the target, the closer to 1.0.
    if "energy" in user_prefs:
        energy_points = 1 - abs(song["energy"] - user_prefs["energy"])
        
        score+= energy_points*2
        reasons.append(f"energy similarity (+{energy_points*2 :.2f})")

    # 4. Tempo similarity: up to 0.5 points, only if the user gave a tempo.
    #    A 100 BPM gap (or more) earns 0; max(0, ...) stops it going negative.
    if "tempo_bpm" in user_prefs:
        tempo_closeness = max(0, 1 - abs(song["tempo_bpm"] - user_prefs["tempo_bpm"]) / 100)
        tempo_points = tempo_closeness * 0.5
        score += tempo_points
        reasons.append(f"tempo similarity (+{tempo_points:.2f})")

    # 5. Return both the total and the explanations as a tuple.
    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Return the top k songs as (song, score, explanation), best score first."""
    scored_songs = []  # will hold one (song, score, explanation) tuple per song

    # 1. Score every song.
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        # Join the list of reasons into one readable string.
        explanation = ", ".join(reasons)
        scored_songs.append((song, score, explanation))

    # 2. Sort from highest score to lowest.
    #    key=... tells sorted() what to compare: item[1] is the score.
    #    reverse=True flips the default low-to-high order.
    ranked = sorted(scored_songs, key=lambda item: item[1], reverse=True)

    # 3. Keep only the top k results.
    return ranked[:k]
