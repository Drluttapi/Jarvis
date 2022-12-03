
import speech_recognition as sr
import pyaudio
import pyttsx3
import wolframalpha
import wikipedia
import datetime
import webbrowser
import subprocess
import pywhatkit
from pyfirmata import Arduino ,SERVO,util
from time import sleep
import os
import random 
import time
import pvporcupine
import struct

#For Servo
port = 'COM3'
pin=10 #Left
pin2 = 9 #Head
pin3 = 8 #Right
pin4 = 13 #led1
board =Arduino(port)

#For servo1
board.digital[pin].mode=SERVO

#For servo2
board.digital[pin2].mode=SERVO

#For servo3
board.digital[pin3].mode=SERVO

#For led
led_1=board.get_pin('d:13:o')

#For servo1 Left
def rotateservo(pin,angle):
    board.digital[pin].write(angle)
    sleep(0.015)

#For servo2 Head 
def servo9(pin2,angle):
    board.digital[pin2].write(angle)
    sleep(0.015)

#For servo3 Right
def servo8(pin3,angle):
    board.digital[pin3].write(angle)
    sleep(0.015)


rotateservo(pin,90)
servo8(pin3,90)

#Times and countdown
def countdown(t):
    while t>0:
        print(t)
        t= t - 1
        time.sleep(1)
    print("Time's up")
    rotateservo(pin,0)
    speak("Time Up")
    speak("Time Up")
    rotateservo(pin,90)

#For music
music = ['C:\\Python\\Python37\\Jarvis_F\\Music\\music2.mp3']
song = random.choice(music)

# Initializations...
running = True
engine = pyttsx3.init()
voices = engine.getProperty('voices')



name = "Jarvis"
engine.setProperty('voice', voices[0].id)


#For a family question
def family():
    speak("I dont have family, I have been programmed by devadath  ")


# Initializations(WolframAlpha).
client = wolframalpha.Client("KYAU62-63QGP34EKH")

# Speak Function...


def speak(text):
    print(f"{name}: {text}")
    engine.say(text)
    engine.runAndWait()


# Listen Function...
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,7)
        

    try:
        print("Recognizing...")    
        command = r.recognize_google(audio, language='en-in')
        print(f"User said: {command}\n")
        
        

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return ''
    return command


def intro():
    speak(f"Hi, I am {name}.")
    speak("I am your virtual assistant!")

print("Connecting to my physical body")

intro()
def conversation():
    while True:
        command = listen().lower()
        if ("exit" or "bye") in command:
            speak("Exiting Program.")
            speak("Thank you for using me!")
            servo8(pin3,30)
            rotateservo(pin,160)
            sleep(2)
            break

        elif "play song" in command:
            speak("What is the title?")
            title = listen()
            pywhatkit.playonyt(title)
            speak(f"Searching for {title} on YouTube!")
            servo9(pin2,60)
            sleep(2)
            servo9(pin2,0)
            break
        
        elif "ok stop" in command:
            break

        elif "take screenshot" in command:
            speak("Capturing Screenshot!")
            pywhatkit.take_screenshot()

        elif "notepad" in command:
            speak("Opening Notepad!")
            servo9(pin2,60)
            subprocess.run('notepad')  
            servo9(pin2,0)
            break

        elif ("shutdown") in command:
            speak("are you Sure ?")
            y=listen()
            if y=="yes" in command:
                speak("You will be Shutdown out in a minute!")
                subprocess.run('shutdown /s')  # To shutdown
                speak("Shutting Down!")
                servo8(pin3,30)
                rotateservo(pin,160)
                
            else :
                speak("OK")
            break

        elif "your name" in command:
            speak("Hello, I am Jarvis!")
            break

        elif "made you" in command:
            rotateservo(pin,0)
            servo8(pin3,170)
            speak("I have been created by Devadath.")
            sleep(2)
            rotateservo(pin,90)
            servo8(pin3,90)
            break

        elif "your father" in command:
            family()
            break

        elif "your mother" in command:
            family()
            break

        elif "family" in command:
            family()
            break

        elif "created you" in command:
            rotateservo(pin,0)
            servo8(pin3,170)
            speak("I have been created by Devadath.")
            sleep(2)
            rotateservo(pin,90)
            servo8(pin3,90)
            break

        elif "who am i" in command:
            
            rotateservo(pin,0)
            servo8(pin3,170)
            speak("If you talk to me then definitely your human.")
            sleep(2)
            rotateservo(pin,90)
            servo8(pin3,90)
            break

        elif "hello" in command:

            speak("Hello ")
            rotateservo(pin,0) ; servo9(pin3,100)
                
            sleep(1)
            rotateservo(pin,90) 
            servo9(pin3,90)
            speak("What is your name")
            N = listen()
            speak("Hello "+ N + ("  ")+"  Nice to know you")
            break
        elif "open minecraft" in command:

            speak("Opening Minecraft")
            mc = "C:\\Users\\kannan\\Desktop\\TLauncher-2.8.jar"
            os.startfile(mc)
            break

        elif "circuit diagram" in command:
            speak("opening my circuit diagram")
            servo9(pin2,60)
            dia="C:\\Users\\kannan\\Downloads\\Jarvis Diagram.png"
            os.startfile(dia)
            sleep(2)
            servo9(pin2,0)
            break

        elif "right" in command:
                servo8(pin3,170)
                speak("Right Hand UP")
                sleep(2)
                servo8(pin3,90)

        elif "left" in command:
                rotateservo(pin,0)
                speak("Left hand UP")
                sleep(0.05)
                rotateservo(pin,90)

        elif "rotate" in command:
                rotateservo(pin,0)
                servo8(pin3,160)
                speak("360 done")
                rotateservo(pin,90)
                servo8(pin3,90)
                break

        elif "sing a song" in command:
            speak(" I dont no how to sing but I can play a song for you here is the song ")
            servo9(pin2,60)
            os.startfile(song)
            sleep(1)
            servo9(pin2,0)
            break

        elif "bye" in command:
            rotateservo(pin,0)
            speak("Good bye !, have a nice day ")
            rotateservo(pin,90)
            speak("Exiting Program.")
            speak("Thank you for using me!")
            servo8(pin3,30)
            rotateservo(pin,160)
            sleep(2)
            break

        elif "cut" in command:
                servo8(pin3,150)
                sleep(1)
                servo8(pin3,80)
                sleep(1)
                servo8(pin3,150)
                sleep(1)
                servo8(pin3,90)
                break

        elif "head" in command:
                servo9(pin2,170)
                sleep(2)
                speak("Done")
                servo9(pin2,0)
                break

        elif "shake hand" in command:
                speak("Touch my right hand")
                sleep(1)

                servo8(pin3,120)
                sleep(0.5)
                servo8(pin3,90)
                sleep(0.5)
                servo8(pin3,110)
                sleep(1)
                servo8(pin3,90)
                speak("Hello Nice to meet you !")
                break

        elif "hands up" in command:
                speak ("O O ")
                rotateservo(pin,0)
                servo8(pin3,170)
                sleep(2)
                rotateservo(pin,90)
                servo8(pin3,90)
                break

        elif "bad" in command:
                speak("Aww am Sad")
                servo9(pin2,170)
                sleep(5)
                servo9(pin2,0)
                break

        elif "dance" in command:
                led_1.write(1)
                rotateservo(pin,0)
                servo8(pin3,0)
                sleep(1)
                rotateservo(pin,150)
                servo8(pin3,170)
                sleep(0.2)
                rotateservo(pin,0)
                servo8(pin3,0)
                sleep(0.1)
                rotateservo(pin,150)
                servo8(pin3,170)
                sleep(0.2)
                rotateservo(pin,90)
                servo8(pin3,90)
                led_1.write(0)
                speak("I dont know exactily how to dance, can you dance for me?")
                break

        elif "who are you" in command:
                speak("I am your virtual assistant Jarvis created by Devadath")
                break
        
        elif "who is jarvis" in command:
            speak("he is an advanced and unique assistant, by the way thats me Lol he he :) ")
            break

        elif "create file" in command:
            speak("Name of the file(without extension).")
            file_name = listen()
            with open(f"{file_name}.txt", 'w') as file:
                speak("Content of the file.")
                file_content = listen()
                file.write(file_content)
                rotateservo(pin,0)
                servo8(pin3,150)
                sleep(1)
                rotateservo(pin,90)
                servo8(pin3,90)
                speak("File created successfully!")
                break

        elif "timer" in command:
            speak("How many seconds to Countdown")
            seconds = listen()
            while not seconds.isdigit():
                speak("That wasn't a number! Please say a number")
                seconds = listen()
            seconds = int(seconds)
            countdown(seconds)

        elif "date" in command:
            date = datetime.now().date()
            speak(f"Today: {date}")
            break

        elif "time" in command:
            servo8(pin3,0)    
            rotateservo(pin,0)
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            servo8(pin3,90)
            rotateservo(pin,90)
            break

        elif "hai" in command:
            speak("haii yoooo !!")
            break

        elif "chief minister of kerala" in command:
            speak("Its pinarayi vijayan")
            break

        elif "google assistant" in command:
            speak("She is a very good and friendly assistant")
            print(":)")
            break

        elif "siri" in command:
            speak("ummmm she is soo good but her father tim cook is not so good !! Lol !!")
            print("Lol!! :D")
            break

        elif "alexa" in command:
            speak("she is amazon's intelligent assistant, also like google,we assistants like to stick together")
            break

        else:
            try:
                if "search" in command:
                    summary = wikipedia.summary(command, sentences=2)
                    print(summary)
                    servo9(pin2,60)
                    speak(summary)
                    servo9(pin2,0)

                else:
                    res = client.query(command)
                    result = res.results
                    servo9(pin2,20)
                    servo8(pin3,110)
                    speak(next(result).text)
                    servo9(pin2,0)
                    servo8(pin3,90)
                    break
            except:
                speak("I can't understand that!")
                print("You can try telling me to search with the question")
                servo9(pin2,0)
                servo8(pin3,90)
#For Wake Up Command
def main():
    porcupine = None
    pa = None
    audio_stream = None 
    print("******* Jarvis is ready ********")
    try:
        porcupine = pvporcupine.create(keywords=["jarvis"],access_key = "LqF2KmVs/OtKb6ZWN8iq1iRGzo6gE14Gcf4qKNBaYrPwEXN/jqurmA==")
        pa = pyaudio.PyAudio()
        audio_stream = pa.open(
                        rate = porcupine.sample_rate,
                        channels=1,
                        format=pyaudio.paInt16,
                        input=True,
                        frames_per_buffer=porcupine.frame_length)
        while True:
            pcm = audio_stream.read(porcupine.frame_length)
            pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

            keyword_index = porcupine.process(pcm)
            if keyword_index >= 0:
                print("Wake up word Detected...",end="")
                led_1.write(1)
                sleep(1)
                led_1.write(0)
                conversation()
                time.sleep(1)
                print("Waiting for your call")
    finally:
        if porcupine is not None:
            porcupine.delete()
        
        if audio_stream is not None:
            audio_stream.close()
       
        if pa is not None:
            pa.terminate()


main()
       
            