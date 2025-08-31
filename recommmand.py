import pandas as pd

# Load dataset
df = pd.read_csv("songs.csv")  # replace with your file

# Convert column names to lowercase for consistency
df.columns = [col.lower() for col in df.columns]

# Function to classify emotion
def predict_emotion_song(df, emotion):
    if emotion == "happy":
        songs = df[(df['valence'] > 0.6) & (df['energy'] > 0.6)]
    elif emotion == "sad":
        songs = df[(df['valence'] < 0.4) & (df['acousticness'] > 0.5)]
    elif emotion == "angry":
        songs = df[(df['energy'] > 0.7) & (df['loudness'] > -6)]
    elif emotion == "fear":
        songs = df[(df['speechiness'] > 0.05) & (df['valence'] < 0.4)]
    elif emotion == "surprise":
        songs = df[(df['tempo'] > 120) | (df['liveness'] > 0.5)]
    elif emotion == "neutral":
        songs = df[(df['valence'] >= 0.4) & (df['valence'] <= 0.6)]
    else:
        return pd.DataFrame()  # return empty if unknown emotion
    
    # Randomly pick 5 songs (if available)
    if len(songs) > 5:
        songs = songs.sample(n=5)
    
    # Return only required columns
    return songs[['artist', 'track', 'url_youtube', 'url_spotify']]

# Example usage
user_emotion = "sad"  # replace with input from user
recommended_songs = predict_emotion_song(df, user_emotion)

print(f"🎵 Recommended songs for {user_emotion} emotion:")
print(recommended_songs.to_string(index=False))