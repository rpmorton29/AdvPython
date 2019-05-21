import json
import matplotlib
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as m3d
import numpy as np
from dateutil import parser
from datetime import date


#Reads Data into a dictionary
def ReadJson():
    json_data = open("tweetsaplenty.json","r")
    newtweet = []
    for line in  json_data:
        line = line.replace(r"\r\n","")
        if r"\"limit\"" not in line:
            newtweet.append(json.loads(json.loads(line)))
    return newtweet

#gets all data needed for 2d graph to be time effecient
def GetData(tweets):
    followers = []
    age = []
    today = date.today()
    belowone =  0
    followers = []
    userid = []
    freq = []
    numtweets = []
    for tweet in tweets:
        cleantext = tweet['user']['created_at'].encode('ascii', "ignore")
        created = parser.parse(cleantext)
        age.append((today.year - created.year - ((today.month, today.day) < (created.month, created.day)))*12)
        if age <1:
            belowone+=1
        followers.append(int(tweet['user']['followers_count']))
    return age,followers

#gets num of tweets when called by 3d plotter
def GetNumTweets(tweets):
    userid = []
    freq = []
    numtweets=[]

    for tweet in tweets:
        if tweet['id'] in userid:
            place = userid.index(tweet['id'])
            freq[place] += 1

        else:
            userid.append(tweet['id'])
            freq.append(1)

    for tweet in tweets:
        place = userid.index(tweet['id'])
        numtweets.append(freq[place])
    return numtweets

#plots the 2d graph with age and follower data
def MakeTwoD(age,followers):

    plt.scatter(age,followers)
    plt.xlabel("Age")
    plt.ylabel("Followers")
    plt.title("Age Vs Followers")
    plt.margins(0)
    plt.show()

#Calls NumTweet func to be effecient when not need to graph 3d graph
def MakeThreeD(tweets,age,followers):
    numtweets = GetNumTweets(tweets)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(age,followers,numtweets, color='red')
    ax.set_xlabel("Age")
    ax.set_ylabel("Followers")
    ax.set_zlabel("# of Tweets")
    ax.set_title("Age Vs Followers Vs Number Of Tweets")
    plt.show()

tweets=ReadJson()
age,follower = GetData(tweets)
#MakeTwoD(age,follower)
MakeThreeD(tweets,age,follower) #uncomment to run 3d plot