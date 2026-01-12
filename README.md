# 🎬 Movie Recommender System

This is a **Movie Recommender System** web application built with **Python** and **Streamlit**. It recommends 5 movies similar to the one selected by the user using a **content-based filtering approach** with movie metadata.

---

## 🚀 Features

- Search and select a movie from the dropdown.
- Get **5 top movie recommendations** based on movie content (genres, keywords, cast, crew, and overview).
- Displays movie posters fetched dynamically from **The Movie Database (TMDB) API**.
- Clean and responsive UI using **Streamlit**.

---

## 🛠 Technologies Used

- **Python 3.11+**
- **Streamlit** – Web app framework for Python.
- **Pandas** – Data manipulation.
- **scikit-learn** – TF-IDF vectorization and cosine similarity.
- **Requests** – Fetch movie posters from TMDB API.
- **NLTK** – Text preprocessing (stemming).

---

## 📁 Files in the Repository

- `app.py` – Main Streamlit app.
- `movie_dict.pkl` – Dictionary of movies used in the app.
- `similarity.pkl` – Precomputed similarity matrix.
- `requirements.txt` – Required Python libraries.
- `.gitignore` – Ignored files and folders.
- `README.md` – Project documentation.

> **Note:** Do **not** commit `.streamlit/secrets.toml` containing your TMDB API key.

---

## 💻 Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/movie-recommender.git
cd movie-recommender

2.Create a virtual environment:

python -m venv venv
# On Mac/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

3.Install dependencies:

pip install -r requirements.txt

4.Add your TMDB API key:

# .streamlit/secrets.toml
[tmdb]
api_key = "YOUR_TMDB_API_KEY"

5.Run the app:

streamlit run app.py
