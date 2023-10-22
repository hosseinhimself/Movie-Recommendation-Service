Welcome file
Welcome file

# Movie Recommendation Service

This repository contains the code and resources for a movie recommendation system built using TF-IDF vectorization and cosine similarity. The system is designed to recommend movies to users based on their preferences and a provided movie title. This README provides an overview of the project, its components, and how to set it up.

## Table of Contents

- [Project Overview](#project-overview)
- [Files and Components](#files-and-components)
- [Docker Hub Availability](#docker-hub-availability)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The Movie Recommendation Service is a content-based recommendation system that suggests movies similar to a given movie title. It utilizes TF-IDF vectorization to process movie data and calculates cosine similarities to identify similar movies. The service provides both a Python API and a Flask web application to make movie recommendations accessible to users.

## Files and Components

### `making_models.py`

- Responsible for preprocessing the movie dataset, applying TF-IDF vectorization, and calculating cosine similarities to build the movie recommendation model.
- Functions and Steps:
  - `combineFeatures(row)`: Combines different features of a movie (genres, director, keywords, cast, popularity) into a single string.
  - Reads movie data from a CSV file (`movie_dataset.csv`).
  - Fills any missing values in specified features with empty strings.
  - Combines specified features into a new feature called `combinedFeatures`.
  - Applies TF-IDF Vectorization on the `combinedFeatures`.
  - Computes cosine similarities between movies based on TF-IDF vectors.
  - Saves the cosine similarity matrix to a file (`movie_similarity.pkl`) using pickle.

### `predict.py`

- Uses the trained model and processed data to recommend movies similar to a provided movie title.
- Functions and Steps:
  - `recommend_movies(movie_title, number_of_movies)`: Recommends movies similar to the given movie title.
  - Loads the movie dataset.
  - Loads the TF-IDF vectorizer and cosine similarities from the saved model (`movie_similarity.pkl`).
  - Finds the closest match to the provided movie title using fuzzy matching.
  - Calculates similarity scores with other movies based on cosine similarities.
  - Returns the closest match (provided movie title) and recommended movies.

### `web_app.py`

- Sets up a Flask web application to provide a user interface for accessing movie recommendations.
- Endpoints:
  1. **POST `/movie`**: Receives a JSON payload with a movie name and the number of recommended movies. Calls the `recommend_movies` function from `predict.py` to generate movie recommendations. Returns the recommendations as JSON.
  2. **GET `/movierecomend`**: Receives movie and counter parameters as query parameters. Calls the `recommend_movies` function from `predict.py` to generate movie recommendations. Returns the recommendations as JSON.


## Docker Hub Availability

The Movie Recommendation Service is available as a Docker container, making it easy to deploy and use in various environments. Whether you're a developer exploring the code or a user interested in the service, Docker offers a convenient way to run the Movie Recommendation Service.

### Docker Image

You can find the Docker image for this project on [Docker Hub](https://hub.docker.com/r/hosseinhimself/recommendersystem). To run the Movie Recommendation Service as a Docker container, use the following command:

```bash
docker run -p 8888:8888 hosseinhimself/recommendersystem
```

After starting the container, the service will be accessible at `http://localhost:8888`. For details on using the service and making movie recommendations, refer to the [Usage](#usage) section.


## Getting Started

To get started with the Movie Recommendation Service, you need to set up the project environment and run the service. Follow these steps to get started:

1. Clone this repository to your local machine:

   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:

   ```bash
   cd Movie-Recommendation-Service
   ```

3. Set up a Python virtual environment:

   ```bash
   python3 -m venv venv
   ```

4. Activate the virtual environment:

   ```bash
   source venv/bin/activate
   ```

5. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Movie Recommendation Service

To run the Movie Recommendation Service, follow these steps:

1. Start the Flask web application:

   ```bash
   python web_app.py
   ```

   The service will be accessible at `http://localhost:8888`.

### Making Movie Recommendations

You can make movie recommendations using the provided endpoints:

1. **POST `/movie`**: Send a JSON payload with a movie name and the number of recommended movies to get recommendations.

   Example usage with cURL:

   ```bash
   curl -X POST -H "Content-Type: application/json" -d '{"movie_name": "example_movie", "movie_numbers": 5}' http://localhost:8888/movie
   ```

2. **GET `/movierecomend`**: Use query parameters for the movie title and the number of recommended movies.

   Example usage in a web browser:

   ```
   http://localhost:8888/movierecomend?movie=example_movie&counter=5
   ```

## Contributing

Contributions to this project are welcome. If you have ideas for improvements or want to report issues, please create a GitHub issue or submit a pull request.
