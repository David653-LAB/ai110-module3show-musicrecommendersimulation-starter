# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

VibeMatch 1.0

---

## 2. Intended Use  

VibeMatch is designed to recommend songs based on a user's musical preferences. It is intended for educational purposes and demonstrates how a basic music recommendation system can work.

The system assumes that users can describe their musical preferences through features such as genre, mood, energy, and tempo. It is designed as a classroom simulation rather than a real-world commercial recommendation platform.

**Non-Intended Use:**

VibeMatch is not intended to replace professional music streaming recommendation systems or guarantee that users will enjoy every recommended song.


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


The system has a limited dataset of only 10 songs which limits the variety of selections. Some genres and moods are not represented equally and may recommend similar songs.



1. **Small dataset:** The recommender only has 10 songs, which limits the variety of recommendations.
2. **Subjective preferences:** Musical taste is personal, so a high score does not always mean someone will enjoy a song.
3. **Fixed scoring weights:** Genre, mood, and energy have predetermined weights. Changing these weights can significantly affect the rankings.
4. **Limited song features:** Although the dataset includes valence, danceability, and acousticness, the current algorithm does not use these features when recommending songs.

---

## 7. Evaluation  

The recommender can be evaluated by testing different user profiles with different preferred genres, moods, and energy levels. The recommendations should be checked to see whether the highest-scoring songs match those preferences.

Additional testing should include comparing results when different feature weights are used and checking whether the system recommends a reasonable variety of songs.

I tested four different user profiles:

High-Energy Pop: Sunrise City ranked first because it matched the pop genre, happy mood, and high energy preferences.

Chill Lofi: Midnight Coding ranked first because it matched both the lofi genre and chill mood, with energy close to the target.

Deep Intense Rock: Storm Runner ranked first because it matched the rock genre and intense mood, with high energy.

Conflicting Preferences: The profile requested ambient music, an intense mood, and high energy. Originally, Spacewalk Thoughts ranked first because genre had the strongest weight, even though its energy was low.

Weight Experiment

I reduced the genre weight from 2 points to 1 point and increased the maximum energy contribution from 1 point to 2 points. After this change, Gym Hero ranked first for the conflicting profile instead of Spacewalk Thoughts.

I was surprised by this result because Gym Hero does not match the requested ambient genre. However, musical preference is subjective, and the experiment demonstrated how changing scoring weights can affect recommendations.

### Comparison Between Profiles

The High-Energy Pop and Deep Intense Rock profiles both preferred high-energy songs, but their top recommendations differed because they requested different genres and moods.

The Chill Lofi profile produced calmer recommendations, such as Midnight Coding and Library Rain, because it prioritized chill music with lower energy.

The Deep Intense Rock profile favored Storm Runner, while the Conflicting Preferences profile originally favored Spacewalk Thoughts because of its ambient genre match.

These results show that changing genre, mood, and energy preferences can produce different recommendations. They also demonstrate that the scoring weights influence which preference matters most.

PS C:\Users\david\codepath-game\ai110-module1show-gameglitchinvestigator-starter\ai110-module3show-musicrecommendersimulation-starter>                                           python -m src.main
Loaded songs: 10

 High-Energy Pop

Top recommendations:

Sunrise City - Score: 3.84
Because: genre match (+1.0), mood match (+1.0), energy similarity(+1.84)

Gym Hero - Score: 2.94
Because: genre match (+1.0), energy similarity (+1.94)

Rooftop Lights - Score: 2.72
Because: mood match (+1.0), energy similarity (+1.72)

Storm Runner - Score: 1.98
Because: energy similarity (+1.98)

Night Drive Loop - Score: 1.70
Because: energy similarity (+1.70)


 Chill Lofi

Top recommendations:

Midnight Coding - Score: 3.96
Because: genre match (+1.0), mood match (+1.0), energy similarity(+1.96)

Library Rain - Score: 3.90
Because: genre match (+1.0), mood match (+1.0), energy similarity(+1.90)

Focus Flow - Score: 3.00
Because: genre match (+1.0), energy similarity (+2.00)

Spacewalk Thoughts - Score: 2.76
Because: mood match (+1.0), energy similarity (+1.76)

Coffee Shop Stories - Score: 1.94
Because: energy similarity (+1.94)


 Deep Intense Rock

Top recommendations:

Storm Runner - Score: 3.98
Because: genre match (+1.0), mood match (+1.0), energy similarity(+1.98)

Gym Hero - Score: 2.94
Because: mood match (+1.0), energy similarity (+1.94)

Sunrise City - Score: 1.84
Because: energy similarity (+1.84)

Rooftop Lights - Score: 1.72
Because: energy similarity (+1.72)

Night Drive Loop - Score: 1.70
Because: energy similarity (+1.70)


 Conflicting Preferences

Top recommendations:

Gym Hero - Score: 2.96
Because: mood match (+1.0), energy similarity (+1.96)

Storm Runner - Score: 2.92
Because: mood match (+1.0), energy similarity (+1.92)

Sunrise City - Score: 1.74
Because: energy similarity (+1.74)

Spacewalk Thoughts - Score: 1.66
Because: genre match (+1.0), energy similarity (+0.66)

Rooftop Lights - Score: 1.62
Because: energy similarity (+1.62)

PS C:\Users\david\codepath-game\ai110-module1show-gameglitchinvestigator-starter\ai110-module3show-musicrecommendersimulation-starter> 


### Additional Profile Comparisons

**High-Energy Pop vs. Chill Lofi:** Sunrise City ranked first for the pop profile, while Midnight Coding ranked first for the lofi profile. This makes sense because they have different genre, mood, and energy preferences.

**High-Energy Pop vs. Conflicting Preferences:** Sunrise City originally performed well for the pop profile, while Spacewalk Thoughts won the conflicting profile because it matched ambient. After changing the weights, Gym Hero ranked first for the conflicting profile because of its high energy and intense mood.

**Chill Lofi vs. Deep Intense Rock:** Midnight Coding ranked first for the chill lofi profile, while Storm Runner ranked first for the rock profile. Their different genres, moods, and energy levels explain the difference.

**Chill Lofi vs. Conflicting Preferences:** Midnight Coding won the chill lofi profile because it matched both genre and mood. The conflicting profile originally favored Spacewalk Thoughts because of its ambient genre match, despite its low energy.

**Deep Intense Rock vs. Conflicting Preferences:** Storm Runner ranked first for the rock profile because it matched both genre and mood. The conflicting profile originally favored Spacewalk Thoughts, but after the weight adjustment, Gym Hero ranked first because energy had more influence.

Before changing the weights, the conflicting profile produced these top results:

- Spacewalk Thoughts: 2.33
- Gym Hero: 1.98
- Storm Runner: 1.96

After changing the weights, Gym Hero ranked first with a score of 2.96. This shows how changing the scoring weights affected the recommendations.
---

## 8. Future Work  

Future improvements could be adding more songs and musical genres to the dataset along with addition features like lyrics, histirt and user feedback.

---

## 9. Personal Reflection  

I learned that music recommendations involve more than matching genres because features like mood, energy, and temp can influence how well a song matches someone's taste. Recommendation systems can introduce bias by repeatedly suggesting similar context which can limit discovery and create an echo chamber.
