import tweepy
import json
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from pprint import pprint
#reads Json into a dictionary
def ReadJson():
    json_data = open("tweetsaplenty.json","r")
    newtweet = []
    for line in  json_data:
        line = line.replace(r"\r\n","")
        if r"\"limit\"" not in line:
            newtweet.append(json.loads(json.loads(line)))
    return newtweet
#converts Unicode text into strings and adds the all times to a list
def CleanTime(tweets):
    time=[]
    for tweet in tweets:
        cleantext = tweet['created_at'][11:16].encode('ascii', "ignore")

        time.append(cleantext)
    return time
    
# Finds the ammount of times a timetamp is in the list
def GetFreq(tweets,times):
    freq = []
    sums =[]

    for time in times:

        if time in freq:
            place = freq.index(time)
            sums[place] += 1

        else:
            freq.append(time)
            sums.append(1)
    return freq,sums

#Plots the data into a line plot
def makeLineGraph(freq,sum):


    plt.plot(freq,sum)
    plt.title('Tweeting Rate During Stream')
    plt.ylabel('Amount of Tweets')
    plt.xlabel('Time(24Hr)')
    plt.xticks(freq[::10],rotation=20)
    plt.margins(0)
    plt.show()

tweets = ReadJson()
times =CleanTime(tweets)
freq,sum = GetFreq(tweets,times)
makeLineGraph(freq,sum)