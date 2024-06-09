import io from 'socket.io-client';

let socket;

export const connectSocket = (setTweets) => {
  socket = io('http://localhost:5000');
  socket.on('new_tweet', (tweet) => {
    setTweets((prevTweets) => [tweet, ...prevTweets]);
  });
};

export const disconnectSocket = () => {
  if (socket) {
    socket.disconnect();
  }
};
