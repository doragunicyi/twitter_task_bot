# -*- coding: utf-8 -*-
import twitter
import csv
import random

SCREEN_NAME = 'DANCERUSH_TASK'

# OAuth
ACCESS_TOKEN_KEY = 'hoge'
ACCESS_TOKEN_SECRET = 'fuga'
CONSUMER_KEY = 'hogehoge'
CONSUMER_SECRET = 'fugafuga'

oauth = twitter.OAuth(ACCESS_TOKEN_KEY,
                      ACCESS_TOKEN_SECRET,
                      CONSUMER_KEY,
                      CONSUMER_SECRET)

# csvから曲データを読み込み
f = open("database.csv", "r")
csv_data = csv.reader(f)
music_data = [ e for e in csv_data]
number = len(music_data)
len_number = int(number) - 1

# Retrieve friends IDs
twitter_api = twitter.Twitter(auth=oauth)
friends = twitter_api.friends.ids(screen_name=SCREEN_NAME, count=5000)
friends_ids = ','.join(map(str, friends['ids']))

stream = twitter.TwitterStream(auth=oauth, secure=True)
for tweet in stream.statuses.filter(follow=friends_ids):
    if tweet['in_reply_to_screen_name']=='DANCERUSH_TASK':
        if '@DANCERUSH_TASK スコアタ課題' in str(tweet) :
            random_number = random.randint(0,len_number)
            tweet_test = '@' + str(tweet['user']['screen_name']) + ' ' + music_data[random_number][0]
            try:
                twitter_api.statuses.update(status=tweet_test)
                print('スコアタ課題')
                print(tweet_test)
            except:
                pass

        elif '@DANCERUSH_TASK プレミアム課題' in str(tweet) :
            random_number = random.randint(0,len_number)
            tweet_test = '@' + str(tweet['user']['screen_name']) + ' ' + music_data[random_number][0]
            try:
                twitter_api.statuses.update(status=tweet_test)
                print('プレミアム課題')
                print(tweet_test)
            except:
                pass
