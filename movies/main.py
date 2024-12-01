from fastapi import FastAPI, HTTPException
from database import get_db
from models import Movie

app = FastAPI()

db = get_db()

@app.get("/movies", response_model=list[Movie])
def get_movies():
    movies = list(db.find({}, {"_id": 0}))
    return movies

@app.get("/movies/{id}", response_model=Movie)
def get_movie(id: str):
    movie = db.find_one({"id": id}, {"_id": 0})
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie
