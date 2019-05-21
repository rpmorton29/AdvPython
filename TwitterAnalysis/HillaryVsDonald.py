import tweepy
import json
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as an
import numpy as np
from pprint import pprint
import mpl_toolkits.mplot3d as m3D

#reads in the Json to a dictionary
def ReadJson():
    json_data = open("tweetsaplenty.json","r")
    newtweet = []
    for line in  json_data:
        line = line.replace(r"\r\n","")

        if r"\"limit\"" not in line:
            newtweet.append(json.loads(json.loads(line)))
    return newtweet

#from the dictionary the times where the key words are mentioned are added to a list
def GetTimes(tweets):

    clinton = []
    trump = []
    for tweet in tweets:

        cleantext = tweet['text'].encode('ascii', "ignore")
        cleantime =tweet['created_at'][11:16].encode('ascii', "ignore")


        if ("hillary" in cleantext.lower()) or ("clinton" in cleantext.lower()):

            clinton.append(cleantime)
        if("donald" in cleantext.lower()) or ("trump" in cleantext.lower()):

            trump.append(cleantime)
    return clinton,trump

#This function finds the amount each time is in the list
def GetClintFreq(tweets,timesclint):
    clintfreq = []
    clintsums =[]

    for time in timesclint:

        if time in clintfreq:
            place = clintfreq.index(time)
            clintsums[place] += 1

        else:
            clintfreq.append(time)
            clintsums.append(1)
    data = np.array([clintfreq,clintsums])
    return clintfreq,clintsums

#This function finds the amount each time is in the list
def GetTrumpFreq(tweets, timestrump):
    trumpfreq = []
    trumpsums =[]

    for time in timestrump:
        if time in trumpfreq:
            place = trumpfreq.index(time)
            trumpsums[place] += 1
        else:
            trumpfreq.append(time)
            trumpsums.append(1)
    return trumpfreq,trumpsums

#starts the plotting of the graphs
def PlotGraphs(clintfreq,clintsums,trumpfreq,trumpsums):
    fig = plt.figure()
    ax = plt.subplot(111)
    xdata, ydata = [], []
    xdata1, ydata1 = [],[]
    ln, = plt.plot([], [],)


    #sets the limit for the graph
    def init():
        ax.set_xlim(clintfreq[0], clintfreq[-1])
        ax.set_ylim(clintsums[0], clintsums[-1])
        return ln,

    #replots the graph to show animation
    def animate(i):


        xdata.append(clintfreq[i])
        xdata1.append(trumpfreq[i])
        ydata.append(clintsums[i])
        ydata1.append(trumpsums[i])
        ax.clear()
        ax.plot(xdata,ydata,label="Hillary or Clinton")
        ax.plot(xdata1, ydata1,label="Donald or Trump")
        plt.xticks(xdata[::10], rotation=20)
        plt.legend()
        plt.title('Keyword Frequency During Stream')
        plt.ylabel('Amount of Tweets')
        plt.xlabel('Time(24Hr)')

    ani = an.FuncAnimation(fig,animate,interval= 1,frames=len(clintfreq),init_func=init,repeat=False)

    plt.show()



tweets = ReadJson()
clinton,trump = GetTimes(tweets)
clintfreq,clintsums = GetClintFreq(tweets,clinton)
trumpfreq,trumpsums=GetTrumpFreq(tweets,trump)
PlotGraphs(clintfreq,clintsums,trumpfreq,trumpsums)
