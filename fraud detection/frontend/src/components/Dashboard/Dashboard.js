import React, { useState, useEffect } from 'react';
import { getCurrentUser } from '../../services/auth';
import TweetList from './TweetList';
import Chart from '../Chart';
import { connectSocket, disconnectSocket } from '../../services/socket';

const Dashboard = () => {
  const [user, setUser] = useState(getCurrentUser());
  const [tweets, setTweets] = useState([]);

  useEffect(() => {
    connectSocket(setTweets);
    return () => {
      disconnectSocket();
    };
  }, []);

  if (!user) {
    return <p>Please log in</p>;
  }

  return (
    <div>
      <h1>Welcome, {user.name}</h1>
      <Chart tweets={tweets} />
      <TweetList tweets={tweets} />
    </div>
  );
};

export default Dashboard;
