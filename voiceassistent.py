import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyaudio
import pyjokes
import pywintypes
import os

def sptext(): #speech to text
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio=recognizer.listen(source)
        try:
            print("Recognizing...")
            data=recognizer.recognize_google(audio)
            return data
        except sr.UnknownValueError: 
            print("Not able to Understand")

def txtspeech(x): #text to speech
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id) #0 for male and 1 for female
    rate=engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(x)
    engine.runAndWait()

if __name__=='__main__':
    
    if "hey nora" in sptext().lower():
        while True:
            data1=sptext().lower()
            if("tell me about you" in data1):
                name="Hello  My name is Nora. I am a voice assistent cerated in python language. You can ask me to tell a joke,ask my age,open youtube or any website,play a song and for ending the conversaion please say exit, How can I help you?"
                txtspeech(name)
            elif("how are you" in data1):
                how="I am fine, hope we are sailing on the same boat"
                txtspeech(how)
            elif("old are you" in data1):
                age="Hello i am 1 hour old"
                txtspeech(age)
            elif("open youtube" in data1):
                webbrowser.open("https://www.youtube.com/")
            elif("tell me a joke" in data1):
                joke_1=pyjokes.get_joke(language="en",category="neutral")
                txtspeech(joke_1)
            elif("play a song" in data1):
                add="D:\gaane"
                listsong=os.listdir(add)
                os.startfile(os.path.join(add,listsong[0]))
            elif("exit" in data1):
                txtspeech("Thank You ! Hopefully I helped you!")
                break
        
    else:
        print("Thank You!")
        
    
    
