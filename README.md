# Movie-Recommendation-Service

This repository contains code for a movie recommendation system using TF-IDF vectorization and cosine similarity.

## Files

### making_models.py

This script (`making_models.py`) is responsible for preprocessing the movie dataset, applying TF-IDF vectorization, and calculating cosine similarities to build the movie recommendation model.

#### Functions and Steps:

- `combineFeatures(row)`: Combines different features of a movie (genres, director, keywords, cast, popularity) into a single string.
- Reads movie data from a CSV file (`movie_dataset.csv`).
- Fills any missing values in specified features with empty strings.
- Combines specified features into a new feature called `combinedFeatures`.
- Applies TF-IDF Vectorization on the `combinedFeatures`.
- Computes cosine similarities between movies based on TF-IDF vectors.
- Saves the cosine similarity matrix to a file (`movie_similarity.pkl`) using pickle.

### predict.py

This script (`predict.py`) uses the trained model and processed data to recommend movies similar to a provided movie title.

#### Functions and Steps:

- `recommend_movies(movie_title, number_of_movies)`: Recommends movies similar to the given movie title.
- Loads the movie dataset.
- Loads the TF-IDF vectorizer and cosine similarities from the saved model (`movie_similarity.pkl`).
- Finds the closest match to the provided movie title using fuzzy matching.
- Calculates similarity scores with other movies based on cosine similarities.
- Returns the closest match (provided movie title) and recommended movies.

### web_app.py

This script (`web_app.py`) sets up a Flask web application to provide a user interface for accessing movie recommendations.

#### Endpoints:

1. **POST `/movie`**:
   - Receives a JSON payload with a movie name and the number of recommended movies.
   - Calls the `recommend_movies` function from `predict.py` to generate movie recommendations.
   - Returns the recommendations as JSON.
   - Example usage:
     ```
     curl -X POST -H "Content-Type: application/json" -d '{"movie_name": "example_movie", "movie_numbers": 5}' http://localhost:8888/movie
     ```

2. **GET `/movierecomend`**:
   - Receives movie and counter parameters as query parameters.
   - Calls the `recommend_movies` function from `predict.py` to generate movie recommendations.
   - Returns the recommendations as JSON.
   - Example usage:
     ```
     http://localhost:8888/movierecomend?movie=example_movie&counter=5
     ```

#### How to Run:

- Start the Flask web application using `app.run()`.
- Access the provided HTTP endpoints to get movie recommendations based on a movie title.

