import React from 'react';

const RecommendedMovie = ({ recommendations }) => {
  if (!recommendations || !recommendations.length) {
    return (
      <div className="recommended-movie">
        <h2>Recommended Movie</h2>
        <p>No recommendation available at the moment.</p>
      </div>
    );
  }

  const recommendation = recommendations[0];
  return (
    <div className="recommended-movie">
      <h2>Recommended Movie</h2>
      <div>
        <h3>{recommendation.title}</h3>
        <img src={recommendation.poster} alt={recommendation.title} width="200" height="200" />
        <p>{recommendation.plot}</p>
      </div>
    </div>
  );
};

export default RecommendedMovie;
