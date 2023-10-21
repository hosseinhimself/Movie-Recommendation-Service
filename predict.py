import pickle
import pandas as pd
from fuzzywuzzy import process


def recommend_movies(movie_title, number_of_movies):
    # Load the movie dataset
    data = pd.read_csv('movie_dataset.csv')

    # Load the TF-IDF vectorizer and cosine similarities from the saved model
    with open('movie_similarity.pkl', 'rb') as file:
        cosine_similarities = pickle.load(file)

    # Find the closest match to the provided movie title
    closest_match = process.extractOne(movie_title, data['original_title'])

    # If the similarity score is below a certain threshold (80%), consider it a mismatch
    if closest_match[1] < 80:
        return "Movie not found. Please try again."
    else:
        # Get the index of the closest match
        idx = data[data['original_title'] == closest_match[0]].index[0]

        # Calculate similarity scores with other movies
        sim_scores = list(enumerate(cosine_similarities[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        # Exclude the movie itself and get the top similar movies
        sim_scores = sim_scores[1:number_of_movies + 1]
        movie_indices = [x[0] for x in sim_scores]

        movies = data[['original_title', 'director', 'release_date', 'genres']].iloc[movie_indices]

        result = {
            'movie_name': data[data['original_title'].isin(closest_match)][['original_title', 'director', 'release_date', 'genres']].to_dict(orient='records'),
            'recommended_movies': movies.to_dict(orient='records')
        }
        # Return the closest match (provided movie title) and recommended movies
        return result


if __name__ == '__main__':

    user_input = input('Enter the movie name: ')
    # Example usage: Recommend movies similar to the user's input
    recommended_movies = recommend_movies(user_input, 5)

    print(recommended_movies)
