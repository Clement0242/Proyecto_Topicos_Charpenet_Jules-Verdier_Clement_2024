import React from 'react';
import axios from 'axios';
import './MoviesGrid.css';

const MoviesGrid = ({ movies, onMovieClick }) => {
  const handleClick = async (movie) => {
    onMovieClick(movie);
    try {
      await axios.post('http://localhost:8001/historial', { movie_id: String(movie.id) });
    } catch (error) {
      console.error('Error registering click in history:', error);
    }
  };  

  return (
    <div className="movies-grid">
      {movies.map((movie) => (
        <div
          key={movie.id}
          className="movie-card"
          onClick={() => handleClick(movie)}
        >
          <img src={movie.poster} alt={movie.title} />
          <h3>{movie.title}</h3>
          <p>{movie.plot}</p>
        </div>
      ))}
    </div>
  );
};

export default MoviesGrid;
