import speech_recognition as sr
from speech_recognition import Microphone
import pyaudio
import time
import pyttsx
import random

#Testing cloudmans edits

def Playback(Audio):
    wf = Audio
    p = pyaudio.PyAudio()
    p.open
    stream = p.open(format=p.get_format_from_width(wf.sample_width),
                    channels=wf.channels,
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
        self.greetings = ('hi','hello','Howdy')
        self.whoami = ('your','name')
    
    def Response(self, command):

        #Recieved a greeting
        if command in self.greetings:
            self.Hello(command)

        #Probably asking for my name    
        elif command in self.whoami:
            self.MyName(command)

            
        elif "ted" in command:
            #if time in command:
                #Time srft time module
            #if date in command:
                #
            if "lights" in command:
                Lights(command)
            if "thank you" in command:
                Welcome(command)
        else:
            self.say('Unknown Command')

    def Hello(self, command):
        #time of day greetings
        self.say(random.choice(self.greetings))

    def Welcome(self, command):    
        print ("You are welcome!")

    def MyName(self, command):
        if "your" in command:
            say('My name is ted')

    ##def Name(command):
    ##    if "my" and "is" in command:
    ##        chop = command.index("is") + 3
    ##        name = command[chop:]
    ##        print "Hi", name, ", How are you?"
    ##    if "what's my" in command:
    ##        try:
    ##            name
    ##            print "You said your name is", name
    ##        except:
    ##            print "You didn't say your name :("

    def Lights(self, command):
        if 'down' in command:
            say("Turning down the lights")
        if 'off' in command:
            say("Turning off the lights")
            
        if 'up' in command:
            say("Turning the lights up")
        if 'on' in command:
            say("Turning on the lights")


    def say(self, text):
        print '[!]', text
        engine.say(text)
        engine.runAndWait()



#INIT

#Set up his voice
engine = pyttsx.init()
engine.setProperty('rate', 120)
ted = engine.getProperty('voices')[0]
engine.setProperty('voice', ted.id)

#Listen for us passively
Recog = sr.Recognizer()
Mic = sr.Microphone()
Recog.energy_threshold = 5000
command = None

#Setup our Results Class
results = Results()

#Inteperet voice if we find it
with Mic as source:
    while True: 
        try:
            print ("[!] Listening")
            audio = Recog.listen(source, 3)
        except:
            sr.WaitTimeoutError
            audio = None
        if audio != None:
            print ("[!] Heard something. ")
            command = Google_VR(audio)
            if type(command) == unicode:
                if command not in ('stop','goodnight'):
                    results.Response(command)    
                else:
                    say('Goodbye')
                    break
