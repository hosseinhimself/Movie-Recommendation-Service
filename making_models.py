import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

def combineFeatures(row):
    return row['genres'] + " " + row['director'] + " " + row['keywords'] + " " + row['cast'] + " " + str(
        row['popularity'])


data = pd.read_csv('movie_dataset.csv')

features = ['genres', 'director', 'keywords', 'cast', 'popularity']

for f in features:
    data[f] = data[f].fillna('')  # Filling all the Null value to empty string

data['combinedFeatures'] = data.apply(combineFeatures, axis = 1)

# TF-IDF Vectorization of genres
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(data['combinedFeatures'])

cosine_similarities = cosine_similarity(tfidf_matrix, tfidf_matrix)

with open('movie_similarity.pkl', 'wb') as file:
    pickle.dump(cosine_similarities, file)




