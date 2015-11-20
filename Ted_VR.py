
import speech_recognition as sr
from speech_recognition import Microphone
import pyaudio
import time
import pyttsx
import random
import datetime

def Playback(Audio):
    wf = Audio
    p = pyaudio.PyAudio()
    p.open
    stream = p.open(format=p.get_format_from_width(wf.sample_width),
                    channels=1,
                    rate=wf.sample_rate,
                    output=True)

    data = wf.frame_data
    print ("You Said:")
    stream.write(data)
    stream.stop_stream()
    stream.close()
    p.terminate()

def Google_VR(audio):
    #Playback(Audio)
    try:
        #this ensures all responses are lower case
        command = (Recog.recognize_google(audio, language = "en-AU")).lower()
        print ("ted thinks you said:", command)
        return command
    except:
        #print "Google has no idea what you said. Try again ?"
        sr.UnknownValueError
        command = None
        return command

class Results:
    def __init__(self):
        self.greetings = ('hi','hello','howdy')
        self.whoami = ('your','name')
        self.time = ('time')
        self.timenow = datetime.datetime.now().strftime("%H:%M ")
        self.weekday = datetime.datetime.now().strftime("%A")
        self.date = datetime.datetime.now().strftime("%d %B %Y ")

    def Response(self, command):
        
        #Recieved a greeting
        for word in self.greetings:
            if word in command:
                self.Hello(command)

        #Probably asking for my name    
        if 'name' in command:
            self.MyName(command)
        elif 'time' in  command:
            self.say(self.timenow)
        elif 'date' in command:
            self.say(self.date)
        elif 'day' in command:
            self.say(self.weekday)
        
            
        elif "ted" in command:
            print 'in'
            if "lights" in command:
                self.Lights(command)
            if "thank you" in command:
                Welcome(command)
        else:
            self.say('Unknown Command')

    def Hello(self, command):
        print "in"
        #time of day greetings
        self.say(random.choice(self.greetings))

    def Welcome(self, command):    
        self.say("You are welcome!")

    def MyName(self, command):
        if "your" in command:
            self.say('My name is ted')
            
    def Lights(self, command):
        if 'down' in command:
            self.say("Turning down the lights")
        if 'off' in command:
            self.say("Turning off the lights")
            
        if 'up' in command:
            self.say("Turning the lights up")
        if 'on' in command:
            self.say("Turning on the lights")


    def say(self, text,):
        print '[!]', text
        engine.say(text)
        engine.runAndWait()

    def gettime(self, command):
        self.say(datetime.date.today().ctime())



#INIT

#Set up his voice
engine = pyttsx.init()
engine.setProperty('rate', 120)
ted = engine.getProperty('voices')[0]
engine.setProperty('voice', ted.id)

#Listen for us passively
Recog = sr.Recognizer()
Mic = sr.Microphone(sample_rate = 10000)

Recog.energy_threshold = 300
#how long to wait after last word
Recog.pause_threshold = 0.7
#don't change the sensitivity over time
Recog.dynamic_energy_threshold = False
# how great the distance is between back. noise and voice. 1 is even 2 is double
Recog.dynamic_energy_adjustment_ratio = 1.5


#Setup our Results Class
results = Results()
x=0

#Inteperet voice if we find it
with Mic as source:
    while True: 
        try:
            try:
                x += 1
                print ("[!] Listening " + str(x))
                audio = Recog.listen(source,1)
            except sr.WaitTimeoutError:
                audio = None
            if audio:
                x=0
                print ("[!] Heard something. ")
                #Playback(audio)
                command = Google_VR(audio)
                if type(command) == unicode:   
                    results.Response(command)    
        except KeyboardInterrupt:
            print "[!] Exiting"
            break
