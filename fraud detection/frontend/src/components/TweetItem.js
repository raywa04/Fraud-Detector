import React from 'react';

const TweetItem = ({ tweet }) => {
  return (
    <div>
      <h3>{tweet.user}</h3>
      <p>{tweet.text}</p>
      <p>Sentiment: {tweet.sentiment}</p>
    </div>
  );
};

export default TweetItem;
