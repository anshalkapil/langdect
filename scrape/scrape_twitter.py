import snscrape.modules.twitter as sntwitter
import pandas as pd
import re

# Define search query and maximum number of tweets to extract
max_tweets = 5000

search_params = " lang:en "
#exclude_user_pattern = re.compile(f".*{search_query}.*", re.IGNORECASE)
# Define list to hold the tweets
tweets_list = []

# Iterate through each tweet using snscrape
for i, tweet in enumerate(sntwitter.TwitterSearchScraper(search_params).get_items()):
     #if not exclude_user_pattern.match(tweet.user.username):
        if i > max_tweets:
            break
        tweets_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])

# Convert the tweets list to a DataFrame
tweets_df = pd.DataFrame(tweets_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])

tweets_df['Datetime'] = tweets_df['Datetime'].apply(lambda x: x.tz_localize(None))

# Save the tweets to an Excel file
tweets_df.to_csv('normal.csv', index=False)

# Print confirmation message
print('Tweets saved to CSV file')