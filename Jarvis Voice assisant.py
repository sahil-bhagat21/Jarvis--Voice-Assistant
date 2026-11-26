import speech_recognition as sr

import webbrowser

import pyttsx3

import musiclibrary


# pip install pocketsphinx

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):

    engine.say(text)

    engine.runAndWait()

def proceesCommand(c):
   print(f"Command received:{c} " )
   if"open google" in c.lower():
       webbrowser.open("http://google.com")
   elif"open facebook" in c.lower():
          webbrowser.open("http://facebook.com")
   elif"open youtube" in c.lower():
          webbrowser.open("http://Youtube.com")
   elif"open brave" in c.lower():
          webbrowser.open("http://Brave.com")
   elif"open chatgpt" in c.lower():
          webbrowser.open("http://Chatgpt.com")
   elif"open Vlc" in c.lower():
          webbrowser.open("http://VLC.com")
   
   elif c.lower().startswith("play"):
        song = c.lower().replace("play ", "").strip()
        if song in musiclibrary.music:
         link = musiclibrary.music[song] 
         webbrowser.open(link)

   else:
        speak("sorry I can't do that")

        

if __name__ == "__main__":

    speak("intitializing Jarvis.....")

    while True :
        # Listen for the wake word "jarvis"

        # obtain audio from the microphone
        r = sr.Recognizer()
    # recognize speech using Sphinx
        try:

            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source , timeout=2 , phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):

                speak("Yaa")

                # listen for command

                with sr.Microphone() as source:
                  print("Jarvis Active...")
                  audio = r.listen(source) 
                  command = r.recognize_google(audio)

                proceesCommand(command)

                

                  
        except sr.UnknownValueError:
            print("jarvis could not understand audio")

        except  Exception as e:

            print("Error ; {0}" .format(e))




    

 

 
