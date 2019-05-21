import tweepy
import json
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from pprint import pprint
#Reads Json into a dictionary
def ReadJson():
    json_data = open("tweetsaplenty.json","r")
    newtweet = []
    for line in  json_data:
        line = line.replace(r"\r\n","")
        if r"\"limit\"" not in line:
            newtweet.append(json.loads(json.loads(line)))
    return newtweet
#finds the number of followers for each user
def GetFollowers(tweets):
    followers = []
    for tweet in tweets:
        followers.append(tweet['user']['followers_count'])
    return followers

#makes a histogram with custom bins and scale to account for the range
#of data that make it unreadable
def MakeHist(followerct):
    data = []
    for num in followerct:
        if not num== 0:
            data.append(num)
    count = np.array(followerct)
    bin = [10,100,500,1000,1500,2000]
    plt.hist(followerct,bin)
    plt.yscale('log')
    plt.xlabel('# of followers')
    plt.ylabel('# of Accounts')
    plt.title('Number of Followers')
    plt.show()


tweets = ReadJson()
followerct = GetFollowers(tweets)
MakeHist(followerct)