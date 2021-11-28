import tweepy
import os

VIDEO_PATH = 'video.mp4'

def post_tweet_with_video():
  auth = tweepy.OAuthHandler(os.environ['CONSUMER_KEY'], os.environ['CONSUMER_SECRET'])
  auth.set_access_token(os.environ['ACCESS_KEY'], os.environ['ACCESS_SECRET'])
  api = tweepy.API(auth)

  media = api.media_upload(VIDEO_PATH)
  api.update_status(status='', media_ids=[media.media_id])

if __name__ == "__main__":
  post_tweet_with_video()
