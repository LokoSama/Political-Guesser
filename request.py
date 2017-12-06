import tweepy,csv,time

ACCESS_TOKEN = '938493239853813762-tlImlRTGU6RraqmBQQQQ3K5klFmHwvG'
ACCESS_SECRET = 'Ga79wDf0YK9YtYc21XEfBH10L0wAttnDL5wQXVT7oNj1J'
CONSUMER_KEY = 'zHK9haWtcpGWHUq12fEMn3Fyw'
CONSUMER_SECRET = 'jIZj1D7jPfXPGSIQTTEGMPgXhIR7lEqyBXRUnudcgpvPDc2wzm'

auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_SECRET)

api = tweepy.API(auth)

public_tweets = api.home_timeline()

# Open/create a file to append data to
csvFile = open('tweets.csv', 'a')

#Use csv writer
csvWriter = csv.writer(csvFile)

for member in tweepy.Cursor(api.list_members, 'cspan', 'members-of-congress').items():
	tweets = api.user_timeline(member.id,count=100)
	time.sleep(0.1)
	for tweet in tweets:
		csvWriter.writerow([tweet.id_str,tweet.user.id, tweet.text.encode('utf-8')])
		
csvFile.close()
