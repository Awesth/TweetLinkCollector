
import tweepy
import re
import credentials


auth = tweepy.OAuthHandler(credentials.consumer_key, credentials.consumer_secret)
auth.set_access_token(credentials.access_token, credentials.access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()

# Function to extract tweets 
def getTweets(username, tweetNr, tweetsList): 
    
    
    # tweets to be extracted 
    tweets = api.user_timeline(screen_name=username) 
  
    tweets_for_csv = [tweet.text for tweet in tweets]
    for j in tweets_for_csv:

        # Check if there is a link in the tweet
        hasLink = re.search('https://', j)
        
        # Appending tweets to the array tmp, if they have a link
        if (hasLink):
            tweetsList.append(j)  

    
    
