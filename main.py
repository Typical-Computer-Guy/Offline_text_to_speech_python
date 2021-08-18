# video on this topic:
# https://youtu.be/IukNmLaTXTA

# pip install pyttsx3
import pyttsx3 # import the required module

engine=pyttsx3.init() # initialize the engine
voices=engine.getProperty('voices') # get the voice property
engine.setProperty('voice',voices[0].id) # set the voice property ---male voice or female voice ...
                                        # for male voice use 0 and for female voice use 1

def speak(sentence): # a function to make the computer say
    engine.say(sentence) # say the sentence
    engine.runAndWait() # wait till the sentence is said

speak("hello, how are you?") # replace the argument of this function with whatever you want the computer to say