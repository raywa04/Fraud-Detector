from flask import request, jsonify
from app import app, db, socketio
from app.models import Tweet
from textblob import TextBlob
import tweepy

auth = tweepy.OAuth1UserHandler(
    app.config['TWITTER_API_KEY'],
    app.config['TWITTER_API_SECRET_KEY'],
    app.config['TWITTER_ACCESS_TOKEN'],
    app.config['TWITTER_ACCESS_TOKEN_SECRET']
)
api = tweepy.API(auth)

@app.route('/api/tweets', methods=['GET'])
def get_tweets():
    keyword = request.args.get('keyword', 'fraud')
    tweets = tweepy.Cursor(api.search, q=keyword, lang="en", tweet_mode='extended').items(100)

    tweet_list = []
    for tweet in tweets:
        sentiment = TextBlob(tweet.full_text).sentiment.polarity
        tweet_entry = Tweet(user=tweet.user.screen_name, text=tweet.full_text, sentiment=sentiment)
        db.session.add(tweet_entry)
        db.session.commit()
        socketio.emit('new_tweet', {
            'user': tweet.user.screen_name,
            'text': tweet.full_text,
            'sentiment': sentiment
        })
        tweet_list.append({
            'user': tweet.user.screen_name,
            'text': tweet.full_text,
            'sentiment': sentiment
        })
    
    return jsonify(tweet_list)
