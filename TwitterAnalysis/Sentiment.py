import json
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from textblob import TextBlob

#Reads the Json into a dictionary
def ReadJson():
    json_data = open("tweetsaplenty.json","r")
    newtweet = []
    for line in  json_data:
        line = line.replace(r"\r\n","")
        if r"\"limit\"" not in line:
            newtweet.append(json.loads(json.loads(line)))
    return newtweet

#calcualtes the sentiment value using the Text blob module
def GetSentiment(tweets):

    pos = []
    neg = []
    for tweet in tweets:

        cleantext = tweet['text'].encode('ascii', "ignore")
        blob = TextBlob(cleantext)
        if blob.sentiment.polarity > 0:
            pos.append(blob.sentiment.polarity)
        elif blob.sentiment.polarity < 0:
            neg.append(abs(blob.sentiment.polarity))
    return pos,neg

#creates a histogram based on the Sentiment value
def MakeHist(positive,negative):
    plt.hist(positive,alpha=.5,label='Positive',color='y')
    plt.hist(negative,alpha=.2,label='Negative',color='m')
    plt.legend()
    plt.title('Tweeting Sentiment During Stream')
    plt.ylabel('Amount of Tweets')
    plt.xlabel('Sentiment Value')
    plt.margins(0)
    plt.show()


tweets =ReadJson()
positive,negative =GetSentiment(tweets)
MakeHist(positive,negative)
