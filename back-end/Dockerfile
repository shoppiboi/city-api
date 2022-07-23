FROM python:3.9-slim

ADD requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

ADD ./src/ /code/
WORKDIR /code

ENV DEBUG=1

ENV BACKEND_HOST=0.0.0.0
ENV BACKEND_PORT=8000

ENV MONGODB_URI=mongodb://mongo_db:27017

ENV CITY_API_HOST=wft-geo-db.p.rapidapi.com
ENV CITY_API_URL=https://wft-geo-db.p.rapidapi.com/v1/geo/cities
ENV CITY_API_KEY=50131d9318mshefc0fa7453e802ap197a13jsna9c8f4971966

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
