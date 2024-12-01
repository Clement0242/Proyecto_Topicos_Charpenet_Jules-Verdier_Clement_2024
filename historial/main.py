from fastapi import FastAPI
from pydantic import BaseModel
import pika
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Agrega el middleware de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas las solicitudes de origen (puedes restringirlo si es necesario)
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos HTTP
    allow_headers=["*"],  # Permite todos los encabezados
)

# Modelo para recibir JSON en el POST
class MovieClick(BaseModel):
    movie_id: str

@app.post("/historial")
def add_to_historial(movie: MovieClick):
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='movie_history')
    channel.basic_publish(exchange='', routing_key='movie_history', body=movie.movie_id)
    connection.close()
    return {"message": "Historial registrado", "movie_id": movie.movie_id}

@app.get("/historial")
def get_historial():
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='movie_history')

    method_frame, header_frame, body = channel.basic_get(queue='movie_history', auto_ack=True)

    if body:
        return {"message": "Historial recuperado", "movie_id": body.decode()}
    else:
        return {"message": "No hay mensajes en el historial"}

    connection.close()
