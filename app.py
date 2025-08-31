import streamlit as st
from Face import get_emotion_from_webcam
from recommmand import predict_emotion_song, df

# Page config
st.set_page_config(page_title="Emotion-Based Music Recommender", page_icon="🎵", layout="centered")

# Custom CSS
st.markdown("""
    <style>
    /* Background */
    .stApp {
        background: linear-gradient(135deg, #1DB954, #191414);
        color: white;
        font-family: 'Segoe UI', sans-serif;
    }

    /* Title */
    h1 {
        color: #fff;
        text-align: center;
        font-size: 2.5rem;
        margin-bottom: 20px;
    }

    /* Buttons */
    div.stButton > button {
        background-color: #1DB954;
        color: white;
        border-radius: 12px;
        font-size: 18px;
        padding: 12px 24px;
        transition: 0.3s;
        border: none;
    }
    div.stButton > button:hover {
        background-color: #1ed760;
        color: black;
        transform: scale(1.05);
    }

    /* Song cards */
    .song-card {
        background-color: #282828;
        padding: 15px;
        border-radius: 15px;
        margin: 10px 0;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
    }
    .song-card h4 {
        margin: 0;
        font-size: 20px;
        color: #1DB954;
    }
    .song-card p {
        margin: 3px 0;
        font-size: 16px;
        color: #ddd;
    }
    .song-links a {
        color: #1DB954;
        margin-right: 15px;
        font-weight: bold;
        text-decoration: none;
    }
    .song-links a:hover {
        text-decoration: underline;
    }
    </style>
""", unsafe_allow_html=True)


# Title
st.title("🎵 Real-Time Music Recommendation System")
st.write("<h3 style='text-align:center;'>Detects your emotion using webcam and recommends songs.</h3>", unsafe_allow_html=True)

# Main logic
if st.button("📸 Capture Emotion"):
    try:
        detected_emotion = get_emotion_from_webcam()
        st.success(f"😊 Detected Emotion: **{detected_emotion}**")

        recommended_songs = predict_emotion_song(df, detected_emotion)

        if not recommended_songs.empty:
            st.subheader("🎶 Recommended Songs")
            for _, row in recommended_songs.iterrows():
                st.markdown(f"""
                <div class="song-card">
                    <h4>{row['track']}</h4>
                    <p>by <i>{row['artist']}</i></p>
                    <div class="song-links">
                        <a href="{row['url_youtube']}" target="_blank">▶️ YouTube</a>
                        <a href="{row['url_spotify']}" target="_blank">🎧 Spotify</a>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.warning("No songs found for this emotion.")
    except Exception as e:
        st.error(f"❌ Error: {e}")
