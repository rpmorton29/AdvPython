import numpy as np
import librosa
import speech_recognition
import matplotlib.pyplot as plt



#Smoothes the audio file to 1s and 0s then convolves to aid in find transitions and pauses
def evenout(signal, sample_rate):


    abs_signal = np.abs(signal)
    window_size = 20

    weights = np.ones(window_size) / window_size

    avg_signal = np.convolve(abs_signal, weights, 'same')

    talking = (avg_signal> .035 )

    for i in range(2):
        talking = (talking > .035)
        talking = talking.astype(np.int)
        for i in range(40):

            window_size = 20

            weights = np.ones(window_size) / window_size

            talking = np.convolve(talking, weights, 'same')

    return talking

#finds the points of pauses and breaks the file into segments. It allows variabled tolerance in the size of pauses
def segment(talking):
    start = False
    n = 0
    k = 0
    splits = []
    timeStamps = []
    gap = .25

    while(np.size(talking)>n):
        if talking[n] >= .03 and  start == False:
            splits.append(n)
            timeStamps.append((n/sample_rate))

            start = True

        elif talking[n]<.03 and start == True:
            k=n
            while np.size(talking)>k:


                if talking[k]<=.03:
                    k+=1
                elif talking[k]>.03:
                    if ((k-n)/sample_rate) <= gap:
                        break
                    else:
                        splits.append(n)
                        timeStamps.append(n/sample_rate)
                        start = False
                        break
                if k == np.size(talking)-1:
                    timeStamps.append(n / sample_rate)
                    splits.append(n)


                k+=1

            n=k
        else:
            n+=1


    return timeStamps,splits

'''finds the gender by running an FFT on each segment. then by taking an average of the magnitude in the male and female
 ranges and comparing them if finds which ever is largest is the assumed gender'''
def findgender(signal,splits):
    gender=[]

    index = 0
    for num in range(len(splits)//2):

        fourier = np.fft.fft(signal[splits[index]:splits[index + 1]])       # converts the time signal into a set of complex numbers in frequency domain

        fourier_mag = np.abs(fourier)   # converts complex numbers into magnitudes for each frequency response

        freq = np.fft.fftfreq(signal[splits[index]:splits[index + 1]].size, d=1. / sample_rate)  # returns array of corresponding frequency for each magnitude




        femaleStart = np.argmax(freq >= 165)
        femaleEnd = np.argmax(freq >= 255)
        femaleAvg = np.mean(fourier_mag[femaleStart:femaleEnd])

        maleStart = np.argmax(freq >= 85)
        maleEnd = np.argmax(freq >= 180)
        maleAvg = np.mean(fourier_mag[maleStart:maleEnd])

        if maleAvg>femaleAvg:
            gender.append("MALE:   ")

        elif maleAvg<femaleAvg:
            gender.append("FEMALE: ")

        index+=2


    return gender


#Using the google API it converts the audio to text segment by segment
def maketext(timeStamps,AudFile):

    myaudio = speech_recognition.AudioFile(AudFile)
    r = speech_recognition.Recognizer()
    speech = []

    first = 0
    second = 1
    for times in range((len(timeStamps)+1)//2):



        with myaudio as source:

            googleaudio = r.record(source, offset=timeStamps[first], duration=((timeStamps[second]-timeStamps[first]+0.2)))


            text = r.recognize_google(googleaudio)
        speech.append(text)

        first+=2
        second+=2
    return speech

#Prints all the data out to a file to be read and examined
def output(gender,speech,timeStamps):
    fout = open('transcript.txt', 'w')
    fout.write("File Converted: "+Audfile + '\n')
    index = 0
    place = 0
    for times in range((len(timeStamps)+1)//2):
        fout.write('{0:27}  {1:10} \n'.format("Time:" + "%.3f" % timeStamps[index]+"-" + "%.3f" % timeStamps[index+1] + " seconds",gender[place] + speech[place]))
        index+=2
        place+=1

Audfile = "schoollife01.wav"
signal,sample_rate = librosa.load(Audfile, sr=None, mono=True)
talking = evenout(signal,sample_rate)
timeStamps,splits =  segment(talking)
gender = findgender(signal,splits)
speech = maketext(timeStamps,Audfile)
output(gender,speech,timeStamps)
