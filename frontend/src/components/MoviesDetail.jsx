import React from 'react';

const MoviesDetail = ({ movie }) => {
  if (!movie) {
    return <div>Selecciona una película para ver los detalles.</div>;
  }

  return (
    <div>
      <h2>{movie.title}</h2>
      <img src={movie.poster} alt={`${movie.title} poster`} />
      <p>{movie.plot}</p>
      <p><strong>Género:</strong> {movie.genre}</p>
    </div>
  );
};

export default MoviesDetail;
