import streamlit as st
import pandas as pd
import pickle
import requests

# =========================
# Load movies and similarity
# =========================
movies_dict = pickle.load(open("movie_dict.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

movies = pd.DataFrame(movies_dict)  # Convert dict back to DataFrame
TMDB_API_KEY = st.secrets["tmdb"]["api_key"]


# =========================
# Function to fetch TMDB poster
# =========================
@st.cache_data(show_spinner=False)
def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US"
        data = requests.get(url, timeout=5).json()
        poster_path = data.get("poster_path")
        if poster_path:
            return "https://image.tmdb.org/t/p/w500" + poster_path
        else:
            return "https://via.placeholder.com/500x750?text=No+Poster"
    except:
        return "https://via.placeholder.com/500x750?text=Error"

# =========================
# Recommendation function
# =========================
def recommend(movie_title, top_n=5):
    if movie_title not in movies['title'].values:
        return ["Movie not found!"]*top_n, ["https://via.placeholder.com/500x750?text=No+Poster"]*top_n

    idx = movies[movies['title'] == movie_title].index[0]
    distances = list(enumerate(similarity[idx]))
    distances = sorted(distances, reverse=True, key=lambda x: x[1])

    recommended_titles = []
    recommended_posters = []

    for i, _ in distances:
        title = movies.iloc[i]['title']
        if title != movie_title and title not in recommended_titles:
            recommended_titles.append(title)
            recommended_posters.append(fetch_poster(movies.iloc[i]['id']))
        if len(recommended_titles) >= top_n:
            break

    return recommended_titles, recommended_posters

# =========================
# Streamlit UI
# =========================
st.set_page_config(page_title="Movie Recommender", layout="wide")
st.title("🎬 Movie Recommender System")
st.write("Select a movie you like and get **5 similar movie recommendations**.")

selected_movie = st.selectbox("Choose a movie:", movies['title'].values)

if st.button("Show Recommendations"):
    names, posters = recommend(selected_movie)

    cols = st.columns(5)
    for i, col in enumerate(cols):
        with col:
            st.image(posters[i], use_container_width=True)
            st.caption(names[i])
