import pickle
import gzip
import os

# Load the original pickle file (which contains a single cosine similarity matrix)
with open('movie_similarity.pkl', 'rb') as f:
    similarity_matrix = pickle.load(f)

# Split the similarity matrix into two parts (or as needed)
split_point = len(similarity_matrix) // 2
matrix1 = similarity_matrix[:split_point]
matrix2 = similarity_matrix[split_point:]

# Create a directory to store the split and compressed parts
os.makedirs('movie_similarity', exist_ok=True)

# Save each part as a separate pickle file
with open('movie_similarity/matrix1.pkl', 'wb') as f:
    pickle.dump(matrix1, f)

with open('movie_similarity/matrix2.pkl', 'wb') as f:
    pickle.dump(matrix2, f)

# Compress each part
for i in range(1, 3):
    input_filename = f'movie_similarity/matrix{i}.pkl'
    output_filename = f'movie_similarity/matrix{i}.pkl.gz'

    with open(input_filename, 'rb') as f_in:
        with gzip.open(output_filename, 'wb') as f_out:
            f_out.writelines(f_in)

    # Remove the original part file
    os.remove(input_filename)

    # Print the compressed file size
    print(f'Saved {output_filename} - Size: {os.path.getsize(output_filename) / (1024 * 1024):.2f} MB')
