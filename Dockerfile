FROM python:3.11.6-alpine3.18

WORKDIR /app

RUN python3 -m venv r_s_venv

COPY ["requirements.txt", "./"]

RUN source r_s_venv/bin/activate

RUN pip install -r requirements.txt

COPY ["movie_similarity.pkl", "movie_dataset.csv", "predict.py" , "web_app.py", "./"]

EXPOSE 8888

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:8888", "web_app:app"]