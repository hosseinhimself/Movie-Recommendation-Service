import requests

url = 'http://localhost:4444/movie'

movie = {
    'movie_name': 'eternal sunshine of the spotless mind',
    'movie_numbers': 5
}

a = requests.post(url, json=movie)

print(a.json())