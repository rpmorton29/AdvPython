import numpy as np
from numpy import random
import random
import math
import matplotlib
import matplotlib.pyplot as plt



def MakeNpData():
    npten = np.random.normal(100,50,10)
    nptenmean = np.mean(npten)

    thousand = np.random.normal(100, 50, 1000)

    tenthousand = np.random.normal(100, 50, 10000)

    hundredthousand = np.random.normal(100, 50, 100000)

    million = np.random.normal(100, 50, 1000000)


    return npten,thousand,tenthousand,hundredthousand,million

def MakeRanData():
    ten =[]
    thou=[]
    tenthou=[]
    hundredthou=[]
    mil=[]
    for i in range(0,10):
        ten.append(random.gauss(100,50))

    for i in range(0,1000):
        thou.append(random.gauss(100,50))

    for i in range(0,10000):
        tenthou.append(random.gauss(100,50))

    for i in range(0,100000):
        hundredthou.append(random.gauss(100,50))

    for i in range(0,1000000):

        mil.append(random.gauss(100,50))
    return ten,thou,tenthou,hundredthou,mil

def MakeGauss():
    guascurve=[]

    x = np.linspace(100 - (5 * 50), 100 + (5 * 50),500)

    ep = (-((x-100)**2/(2*50**2)))
    exp = np.exp(ep)
    sq =(1/np.sqrt(2*np.pi*50**2))
    gauss = sq*exp
    return gauss,x

def PlotGausCurve(gauss, x,million):
    million = np.array(million)
    fig , ax = plt.subplots()
    ax.plot(x,gauss,alpha=1)

    #the annontations were functioning corretly with the inlaid histogram in the process of completinf the program it
    #stopped and I was unable to debug it
    ax.annotate("MU",(100,1),xytext = (120,1),arrowprops={'arrowstyle': '->'})
    ax.annotate("MU+/_SIGMA", (100+50, .30), xytext=(170, .2), arrowprops={'arrowstyle': '->'})
    ax.annotate("MU+/_SIGMA", (100-50, .30), xytext=(170, .2), arrowprops={'arrowstyle': '->'})
    ax.annotate("MU+/_ 2SIGMA", (100 +100, .01), xytext=(25, .1), arrowprops={'arrowstyle': '->'})
    ax.annotate("MU+/_ 2SIGMA", (100 - 100, .01), xytext=(25, .1), arrowprops={'arrowstyle': '->'})
    ax.annotate("MU+/_ 3SIGMA", (100 + 150, .01), xytext=(35, .18), arrowprops={'arrowstyle': '->'})
    ax.annotate("MU+/_ 3SIGMA", (100 - 150, .01), xytext=(35, .18), arrowprops={'arrowstyle': '->'})

    ax2= ax.twinx()
    ax2.hist(million,bins=50,alpha=.2)
    plt.title('Guassian Curve')
    plt.show()


def GetRanError(ten,thou,tenthou,hundredthou,mil):
    avgranderror =[]
    truedata = MakeGauss()


    tenmean = np.mean(ten)
    tenstd = np.std(ten)
    tenerror = makeGuasserros(tenmean,tenstd)
    tenerror = np.abs(tenerror-truedata)
    avgranderror.append(np.average(tenerror))

    thoumean = np.mean(thou)
    thoustd = np.std(thou)
    thouerror = makeGuasserros(thoumean, thoustd)
    thouerror = np.abs(thouerror - truedata)
    avgranderror.append(np.average(thouerror))

    tenthoumean = np.mean(tenthou)
    tenthoustd = np.std(tenthou)
    tenthouerror = makeGuasserros(tenthoumean, tenthoustd)
    tenthouerror = np.abs(tenthouerror - truedata)
    avgranderror.append(np.average(tenthouerror))

    hundredthoumean = np.mean(hundredthou)
    hundredthoustd = np.std(hundredthou)
    hundredthouerror = makeGuasserros(hundredthoumean, hundredthoustd)
    hundredthouerror = np.abs(hundredthouerror - truedata)
    avgranderror.append(np.average(hundredthouerror))

    milmean = np.mean(mil)
    milstd = np.std(mil)
    milerror = makeGuasserros(milmean, milstd)
    milerror = np.abs(milerror - truedata)
    avgranderror.append(np.average(milerror))

    return avgranderror

def GetNPError(npten,thousand,tenthousand,hundredthousand,million):
    avgnperror=[]
    truedata = MakeGauss()
    nptenmean = np.mean(npten)
    nptenstd = np.std(npten)

    nptenerror = makeGuasserros(nptenmean,nptenstd)
    nptenerror = np.abs(nptenerror-truedata)
    avgnperror.append(np.average(nptenerror))

    npthousandmean = np.mean(thousand)
    npthousandstd = np.std(thousand)
    npthousanderror = makeGuasserros(npthousandmean, npthousandstd)
    npthousanderror = np.abs(npthousanderror - truedata)
    avgnperror.append(np.average(npthousanderror))


    nptenthousandmean = np.mean(tenthousand)
    nptenthousandstd = np.std(tenthousand)
    nptenthousanderror = makeGuasserros(nptenthousandmean, nptenthousandstd)
    nptenthousanderror = np.abs(nptenthousanderror - truedata)
    avgnperror.append(np.average(nptenthousanderror))


    nphundredthousandmean = np.mean(hundredthousand)
    nphundredthousandstd = np.std(hundredthousand)
    nphundredthousanderror = makeGuasserros(nphundredthousandmean, nphundredthousandstd)
    nphundredthousanderror = np.abs(nphundredthousanderror - truedata)
    avgnperror.append(np.average(nphundredthousanderror))

    npmillionmean = np.mean(million)
    npmillionstd = np.std(million)
    npmillionerror = makeGuasserros(npmillionmean,npmillionstd)
    npmillionerror = np.abs(npmillionerror-truedata)
    avgnperror.append(np.average(npmillionerror))

    return avgnperror

def makeGuasserros(MU,SIG):
    x = np.linspace(100 - (5 * 50), 100 + (5 * 50), 500)
    ep = (-((x - MU) ** 2 / (2 * SIG ** 2)))
    exp = np.exp(ep)
    sq = (1 / np.sqrt(2 * np.pi * SIG ** 2))
    gauss = sq * exp
    return gauss


def ploterrorplots(avgnperror,avgranderror):

    x=[1,2,3,4,5]
    y_pos = np.arange(len(avgnperror))
    plt.subplot(2,1,1)
    plt.bar(y_pos,avgnperror,alpha=.4,color='y')
    y_pos = np.arange(len(avgranderror))
    plt.subplot(2, 1, 1)
    plt.bar(y_pos, avgranderror,alpha=.2,color='m')

    plt.legend(loc='right')
    plt.title('Error in Rand VS NP')
    avgtotalnp = sum(avgnperror)
    avgtotalrand = sum(avgranderror)
    if avgtotalnp > avgtotalrand:
        color = 'y'
    else:
        color = 'm'
    plt.subplot(2,1,2)
    y_pos = [1]
    plt.subplot(2, 1, 2)
    plt.bar(y_pos, avgtotalnp, alpha=.4, color=color)
    y_pos = [1]
    plt.subplot(2, 1, 2)
    plt.bar(y_pos, avgtotalrand, alpha=.4, color=color)
    plt.show()

npten,thousand,tenthousand,hundredthousand,million= MakeNpData()
avgnperror=GetNPError(npten,thousand,tenthousand,hundredthousand,million)
ten,thou,tenthou,hundredthou,mil=MakeRanData()
avgranderror=GetRanError(ten,thou,tenthou,hundredthou,mil)
gauss,x = MakeGauss()
PlotGausCurve(gauss,x,million)
ploterrorplots(avgnperror,avgranderror)