from fastapi import FastAPI
import pika
import random
import requests
from collections import Counter
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/recomendar")
def recomendar():
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='movie_history')

    method_frame, header_frame, body = channel.basic_get(queue='movie_history', auto_ack=True)
    historial = []

    while body:
        historial.append(body.decode())
        method_frame, header_frame, body = channel.basic_get(queue='movie_history', auto_ack=True)

    connection.close()

    if not historial:
        return {"message": "No hay historial para generar recomendaciones."}

    response = requests.get("http://movies:8000/movies")
    if response.status_code != 200:
        return {"message": "Error al comunicarse con el microservicio de películas."}

    all_movies = response.json()

    peliculas_vistas = [pelicula for pelicula in all_movies if pelicula['id'] in historial]
    generos_vistos = [pelicula['genre'] for pelicula in peliculas_vistas]

    if not generos_vistos:
        return {"message": "No se encontraron géneros en el historial para generar recomendaciones."}

    genero_preferido = Counter(generos_vistos).most_common(1)[0][0]

    peliculas_recomendadas = [
        pelicula for pelicula in all_movies 
        if pelicula['id'] not in historial and pelicula['genre'] == genero_preferido
    ]

    if peliculas_recomendadas:
        recomendacion = random.choice(peliculas_recomendadas)
        return {"recomendacion": recomendacion}
    else:
        return {"message": f"No se encontraron películas de género {genero_preferido} para recomendar."}
