import pickle
import gzip
import os

# Function to combine and load a model
def combine_models():
    combined_matrix = []

    # Iterate over the split models
    for i in range(1, 3):
        compressed_filename = f'movie_similarity/matrix{i}.pkl.gz'
        decompressed_filename = f'movie_similarity/matrix{i}.pkl'

        # Decompress the model
        with gzip.open(compressed_filename, 'rb') as f_in:
            with open(decompressed_filename, 'wb') as f_out:
                f_out.write(f_in.read())

        # Load the decompressed model
        with open(decompressed_filename, 'rb') as f:
            matrix_part = pickle.load(f)

        # Combine the matrix parts
        combined_matrix.extend(matrix_part)

        # Remove the decompressed part file
        os.remove(decompressed_filename)

    return combined_matrix

# Combine the models
combined_model = combine_models()

# Optionally, save the combined model as a pickle file
with open('combined_model.pkl', 'wb') as f:
    pickle.dump(combined_model, f)

print('Models combined and saved as combined_model.pkl')
