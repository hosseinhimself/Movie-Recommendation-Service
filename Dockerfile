FROM python:3.11.6-slim

WORKDIR /app

# Copy the requirements file to the /app directory
COPY requirements.txt .

# Create a Python virtual environment
RUN python3 -m venv r_s_venv

# Activate the virtual environment and install requirements within a single RUN instruction
RUN /bin/bash -c "source r_s_venv/bin/activate && pip install -r requirements.txt"

COPY ["movie_similarity.pkl", "movie_dataset.csv", "predict.py", "web_app.py", "./"]

EXPOSE 8888

ENTRYPOINT ["/app/r_s_venv/bin/gunicorn", "--bind=0.0.0.0:8888", "web_app:app"]
