import React, { useState, useEffect } from 'react';
import axios from 'axios';
import MoviesGrid from './components/MoviesGrid';
import RecommendedMovie from './components/RecommendedMovie';

const App = () => {
  const [movies, setMovies] = useState([]);
  const [selectedMovie, setSelectedMovie] = useState(null);
  const [recommended, setRecommended] = useState([]);
  const [clickCount, setClickCount] = useState(0);

  useEffect(() => {
    const fetchMovies = async () => {
      const response = await axios.get('http://localhost:8003/random?count=10');
      setMovies(response.data);
    };
    fetchMovies();
  }, []);

  const handleMovieClick = async (movie) => {
    setSelectedMovie(movie);
    setClickCount((prev) => prev + 1);

    try {
      await axios.post('http://localhost:8001/historial', { movie_id: String(movie.id) });
    } catch (error) {
      console.error('Error registering click in history:', error);
    }

    if ((clickCount + 1) % 3 === 0) {
      try {
        const response = await axios.get('http://localhost:8002/recomendar');
        setRecommended([response.data.recomendacion]);
      } catch (error) {
        console.error('Error fetching recommendations:', error);
      }
    }
  };

  return (
    <div>
      <h1>Movie Recommender</h1>
      <MoviesGrid movies={movies} onMovieClick={handleMovieClick} />
      {selectedMovie && (
        <div>
          <h2>Selected Movie: {selectedMovie.title}</h2>
          <p>{selectedMovie.plot}</p>
        </div>
      )}
      <RecommendedMovie recommendations={recommended} />
    </div>
  );
};

export default App;
