import speech_recognition as sr
from speech_recognition import Microphone
import pyaudio
import time
import pyttsx
import random


def Playback(Audio):
    wf = Audio
    p = pyaudio.PyAudio()
    p.open
    stream = p.open(format=p.get_format_from_width(wf.sample_width),
                    channels=wf.channels,
                    rate=wf.sample_rate,
                    output=True)

    data = wf.frame_data
    print "You Said:"
    stream.write(data)
    stream.stop_stream()
    stream.close()
    p.terminate()

def Google_VR(audio):
    #Playback(Audio)
    try:
        #this ensures all responses are lower case
        command = (Recog.recognize_google(audio, language = "en-AU")).lower()
        print "ted thinks you said:", command
        return command
    except:
        #print "Google has no idea what you said. Try again ?"
        sr.UnknownValueError
        command = None
        return command
    
def Results(command):
    if 'hello' in command:
        Hello(command)
    if "name" and "your" in command:
        MyName(command)
    if "ted" in command:
        #if time in command:
            #Time srft time module
        #if date in command:
            #
        if "lights" in command:
            Lights(command)
        if "thank you" in command:
            Welcome(command)
    else:
        say('Unknown Command')

def Hello(command):
    #time of day greetings
    greetings = ('hi','hello','hola')
    say(random.choice(greetings))

def Welcome(command):    
    print "You are welcome!"

def MyName(command):
    if "your" in command:
        say('My name is ted, cunt')
        say('Who the fuck are you?')
        say('haha, just kidding you cunt')

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

def Lights(command):
    if 'down' in command:
        say("Turning down the lights for you")
    if 'up' in command:
        say("Turning the lights up")


def say(text):
    print text
    engine.say(text)
    engine.runAndWait()



#INIT

#Set up her voice
engine = pyttsx.init()
engine.setProperty('rate', 120)
ted = engine.getProperty('voices')[0]
engine.setProperty('voice', ted.id)

#Listen for us passively
Recog = sr.Recognizer()
Mic = sr.Microphone()
Recog.energy_threshold = 6000
command = None

#Inteperet voice if we find it
with Mic as source:
    while True: 
        try:
            print "listening"
            audio = Recog.listen(source, 10)
        except:
            sr.WaitTimeoutError
            audio = None
        if audio != None:
            print "busy. Not listening"
            print "heard something"
            command = Google_VR(audio)
            if type(command) == unicode:
                Results(command)
                if "good night ted" in command:
                    break
               
        
        
print "Goodnight", name
