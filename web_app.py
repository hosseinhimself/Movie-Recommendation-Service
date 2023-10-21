import predict
from flask import Flask, request, jsonify

app = Flask('Movie_recommendation_system')


@app.route('/movie', methods=['POST'])
def recommender():
    movie = request.get_json()
    return jsonify(predict.recommend_movies(movie['movie_name'], movie['movie_numbers']))


# example: http://localhost:8888/movierecomend?movie=eternalsunshinofthespotlessmind&counter=5
@app.route('/movierecomend', methods=['GET'])
def show_user_profile():
    movie_name = request.args.get('movie')
    movie_numbers = request.args.get('counter', type=int)  # Extract 'counter' as an integer
    if movie_numbers is None:
        movie_numbers = 5
    return jsonify(predict.recommend_movies(movie_name, movie_numbers))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8888)
