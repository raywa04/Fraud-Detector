import React from 'react';
import TweetItem from '../TweetItem';

const TweetList = ({ tweets }) => {
  return (
    <div>
      {tweets.map((tweet) => (
        <TweetItem key={tweet.id} tweet={tweet} />
      ))}
    </div>
  );
};

export default TweetList;
