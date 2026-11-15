# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

VibeMatch 1.0

---

## 2. Intended Use  

VibeMatch is designed to recommend songs based on a user's musical preferences. It is intended for educational purposes and demonstrates how a basic music recommendation system can work.

The system assumes that users can describe their musical preferences through features such as genre, mood, energy, and tempo. It is designed as a classroom simulation rather than a real-world commercial recommendation platform.


---

## 3. How the Model Works  

The model uses content-based filtering to compare song characteristics with a user's preferences. It considers features such as genre, mood, energy, and tempo.

Each song receives a score based on how closely its characteristics match the user's preferences. Different features can have different weights depending on their importance. The system then ranks songs by their scores and recommends the highest-scoring matches.

---

## 4. Data  

The model uses a dataset containing 10 songs. Each song includes information such as its title, artist, genre, mood, energy, tempo, valence, danceability, and acousticness.

The dataset includes genres such as pop, lofi, rock, ambient, jazz, synthwave, and indie pop. The moods include happy, chill, intense, relaxed, moody, and focused.

The dataset is relatively small and does not represent every musical genre or listening preference. It also does not include information such as song lyrics, listening history, or user likes and dislikes.

---

## 5. Strengths  

The system can identify songs that share similar characteristics with a user's preferences. It can recommend music based on genre, mood, energy, and tempo. Its scoring approach is also relatively simple to understand and explain.

---

## 6. Limitations and Bias 


The system has a limited dataset of only 10 songs which limits the variety of selections. Some gneres and moods are not represnted equally and may recoomend similar songs.

---

## 7. Evaluation  

The recommender can be evaluated by testing different user profiles with different preferred genres, moods, and energy levels. The recommendations should be checked to see whether the highest-scoring songs match those preferences.

Additional testing should include comparing results when different feature weights are used and checking whether the system recommends a reasonable variety of songs.

---

## 8. Future Work  

Future imporvemnets could be adding more songs and musical genres to the dataset along with addition features like lyrics, histirt and user feedback.

---

## 9. Personal Reflection  

I learned that music recommendations involve more than matching genres because features like mood, energy, and temp can influence how well a song matches someone's taste. Recommendation systems can introduce bias by repeatedly suggesting similar context which can limit discovery and create an echo chamber.
