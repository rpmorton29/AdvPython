import tweepy
import json
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from pprint import pprint


#reads Json into dictionary
def ReadJson():
    json_data = open("tweetsaplenty.json","r")
    newtweet = []
    for line in  json_data:
        line = line.replace(r"\r\n","")
        if r"\"limit\"" not in line and "retweeted_status" in line:
            newtweet.append(json.loads(json.loads(line)))
    return newtweet


#finds the top 10 rts from RTcount in RT status
def gettop(newtweet):
    rtcount = []
    for tweet in newtweet:
        rtcount.append(tweet['retweeted_status']['retweet_count'])
    sort = np.array(rtcount)
    toptenind = np.argpartition(sort, -10)[-10:]
    return toptenind,sort

#Plots the Data into a bar graph
def makeGraph(topten,sort,newtweet):
    rts = []
    users = []
    fig, ax = plt.subplots()
    for ind in topten:
        rts.append(newtweet[sort[ind]]['retweeted_status']['retweet_count'])
        users.append(newtweet[sort[ind]]['user']['name'])
    y_pos = np.arange(len(users))
    plt.bar(y_pos, sorted(rts,reverse=True), align='center',alpha=1,color=['black', 'red', 'green', 'blue', 'orange'])
    plt.xticks(y_pos,users,rotation='vertical')
    plt.ylabel('Number of Retweets')
    plt.title('Top Retweeted')
    plt.show()

newtweet = ReadJson()
topten,sort = gettop(newtweet)
makeGraph(topten,sort,newtweet)
