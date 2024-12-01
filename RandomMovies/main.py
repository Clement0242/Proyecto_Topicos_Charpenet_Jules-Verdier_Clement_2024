from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import httpx
import random

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"], 
)

MOVIES_SERVICE_URL = "http://movies:8000/movies"

@app.get("/random")
async def get_random_movies(count: int = 5):
    async with httpx.AsyncClient() as client:
        response = await client.get(MOVIES_SERVICE_URL)
        if response.status_code != 200:
            raise HTTPException(status_code=500, detail="Error fetching movies")

        movies = response.json()
        if len(movies) < count:
            raise HTTPException(status_code=400, detail="Not enough movies available")

        return random.sample(movies, count)
