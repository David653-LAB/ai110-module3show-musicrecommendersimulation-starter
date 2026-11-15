# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

This project simulates a music recommendation system that suggests songs based on a user's musical preferences. It uses song attributes such as genre, mood, energy, and tempo to calculate recommendation scores and rank songs based on how closely they match the user's taste.

---

## How The System Works

Explain your design in plain language.

Our music recommendation system uses content-based filtering to suggest songs based on a user's musical preferences.

Each Song contains information such as its title, artist, genre, mood, energy, tempo, valence, danceability, and acousticness.

The UserProfile stores the user's preferred genres and moods, along with numerical preferences such as energy, tempo, and valence.

The Recommender compares each song's features with the user's preferences and calculates a weighted score. Songs that match the user's preferences more closely receive higher scores.

Finally, the system ranks songs from highest score to lowest score and recommends the best matches to the user.


INPUT
User Preferences
(genre, mood, target energy, target tempo)
        |
        v
PROCESS
Loop through every song in songs.csv
Calculate genre, mood, energy, and tempo points
Add the points to get a total score
        |
        v
OUTPUT
Sort songs by total score
Display the Top 5 recommendations

Algorithm Recipe
- Genre match: +2.0 points.
- Mood match: +1.0 point.
- Energy similarity: up to +1.0 point.
- Tempo similarity: up to +0.5 points.
- Sort songs by total score, highest first, and return the Top 5.
Expected Biases
- Genre has the largest weight, so recommendations may over-prioritize a user's favorite genre.
- Tempo and energy can overlap, potentially giving similar musical characteristics extra influence.
- Exact genre and mood matching may penalize songs that are similar but use different labels.



---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

```text
Loaded songs: 10

Top recommendations:

Sunrise City - Score: 3.98
Because: genre match (+2.0), mood match (+1.0), energy similarity (+0.98)

Gym Hero - Score: 2.87
Because: genre match (+2.0), energy similarity (+0.87)

Rooftop Lights - Score: 1.96
Because: mood match (+1.0), energy similarity (+0.96)

Night Drive Loop - Score: 0.95
Because: energy similarity (+0.95)

Storm Runner - Score: 0.89
Because: energy similarity (+0.89)
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



