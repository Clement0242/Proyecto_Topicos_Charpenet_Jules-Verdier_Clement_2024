from pydantic import BaseModel

class Movie(BaseModel):
    id: str
    title: str
    poster: str
    plot: str
    genre: str
