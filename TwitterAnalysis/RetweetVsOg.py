import tweepy
import json
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from pprint import pprint
#reads json into dictionary
def ReadJson():
    json_data = open("tweetsaplenty.json","r")
    newtweet = []
    for line in  json_data:
        line = line.replace(r"\r\n","")
        if r"\"limit\"" not in line:
            newtweet.append(json.loads(json.loads(line)))

    return newtweet

#determines if it is a orginal tweet or rt
def GetType(tweets):
    rt = 0
    og = 0
    for tweet in tweets:
        if "RT" in tweet['text']:
            rt +=1
        else:
            og +=1
    return(rt,og)


#Makes bar graph from the data
def MakeBarh(retweetct,originalct):
    data =[originalct,retweetct]
    y_pos = np.arange(len(data))
    plt.barh(y_pos, data, align='center', alpha=1)
    plt.yticks(y_pos, [ "Originals","Retweets"], rotation=20)
    plt.xlabel('Amount of Tweet Kind')
    plt.ylabel('Tweet kind')
    plt.title('Original Tweets  Vs Retweets')
    plt.show()



tweets = ReadJson()
retweetct, originalct= GetType(tweets)
MakeBarh(retweetct,originalct)