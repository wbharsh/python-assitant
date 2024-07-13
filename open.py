
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import subprocess as sp
import smtplib
import requests, json
#import openai, json does not use chatgpt currently
import pywhatkit


 ### openweather API for temprature started

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius=kelvin-273.15
    fahrenheit=celsius*(9/5)+32
    return celsius,fahrenheit

BASE_URL="http://api.openweathermap.org/data/2.5/weather?"



api_key="api key from openweather site"
CITY='Ujjain'
url=BASE_URL + "appid=" + API_KEY + "&q=" + CITY
response = requests.get(url).json()
temp_kelvin=response['main']['temp']
temp_celsius, temp_fahrenheit=kelvin_to_celsius_fahrenheit(temp_kelvin)
wind_speed=response['wind']['speed']
humidity=response['main']['humidity']
description=response['weather'][0]['description']
sunrise_time=datetime.datetime.utcfromtimestamp(response['sys']['sunrise']+response['timezone'])
sunset_time=datetime.datetime.utcfromtimestamp(response['sys']['sunset']+response['timezone'])

# open files


paths = {
    'notepad': "C:\\Program Files\\Notepad++\\notepad++.exe",
    'discord': "C:\\Users\\ashut\\AppData\\Local\\Discord\\app-1.0.9003\\Discord.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe"
}


#open this file
def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)
def open_notepad():
    os.startfile(paths['notepad'])

def open_discord():
    os.startfile(paths['discord'])
def open_calculator():
    sp.Popen(paths['calculator'])


#find ip add
def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]

def play_on_youtube(video):
    pywhatkit.playonyt(video)
def search_on_google(query):
    pywhatkit.search(query)
def send_whatsapp_message(number, message):
    pywhatkit.sendwhatmsg_instantly(f"+91{number}", message)




###open weather API close

#voice 3 is in use
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#starting wish
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    
    elif hour>=12 and hour<18:
        speak("Good afternoon!")
    
    else:
        speak("Good Evening!")
    speak("")

    speak("this is jency, how may i help you")

#taking input through voice
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        audio=r.listen(source)
    try:
        print("Recognizing....")
        query=r.recognize_google(audio,  language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        print("say that again")
        return "None"
    return query

#sending email
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('YOUR GMAIL','PASSWARD')
    server.sendmail('YOUR GMAIL',to,content)
    server.close()

#############################               MAIN    CLASS  started        #############
if __name__== "__main__":

  wishMe()

  while True:
            query = takeCommand().lower()
#wikipedia
            if 'wikipedia' in query:
                speak('searching Wikipedia....')
                query=query.replace("wikipedia","")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
#web browser
            elif 'youtube' in query:
                speak('which vedio')

                query=takeCommand().lower
                if query!="say that again":
                    vedio=query
                    play_on_youtube(vedio)

             
            elif 'google' in query:
                webbrowser.open("google.com")
            
 #hey           
            elif 'hi' in query:
                speak("hey sir what's up")

            
 #music           
            elif 'play music' in query:
                music_dir='C:\\jency\\music'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir,songs[0]))
 #gellary           
            elif 'open picture' in query:
                pic='C:\\jency\\pic'
                picture = os.listdir(pic)
                print(picture)
                os.startfile(os.path.join(pic,picture[0]))
 #time           
            elif 'time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")
#send mail
            elif 'send mail' in query:
                try:
                    speak("what should i say")
                    content=takeCommand()
                    to='SEND TO MAIL ID'
                    sendEmail(to,content)
                    speak("Email has been send")
                except Exception as e:
                    print(e)
                    speak("sorry unable to send this")
#city details
            elif 'ujjain information' in query:
                print("you are in Ujjain")
                print(f" Temprature in {CITY}: {temp_celsius:.2f}C or {temp_fahrenheit}F")    
                print(f"Humidity in {CITY}: {humidity}%")
                print(f"WIND SPEED in {CITY}: {wind_speed}m/s")
                print(f"Genral Weather in {CITY}: {description}")
                print(f"Sun Rise in {CITY} at {sunrise_time}")
                print(f"Sun Set in {CITY} at {sunset_time}")
                speak("you are in Ujjain sir")
                speak(f"Temprature {temp_celsius:.2f} degree celsius")
                speak(f"Huidity {humidity} persectage")
                speak(f"Wind speed {wind_speed} meter per secound")
                speak(f"the weather is {description}")
                speak(f"sun rise of {sunrise_time}")
                speak(f"sunset of {sunset_time}")
 #exit           
            elif 'stop' in query:
                speak('its time to take rest')
                speak('bye bye')
                break
                

