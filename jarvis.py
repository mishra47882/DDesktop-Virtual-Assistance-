import pyttsx3 
import datetime
import speech_recognition as sr 
import wikipedia 
import smtplib
import webbrowser
import os
 
engine=pyttsx3.init('sapi5')
voice=engine.getProperty('voice')
engine.setProperty('voice', voice[1])

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning")
    if hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening")
    speak('I am vishal sir. please tell me how may i hepl you')


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening..")
        r.pause_threshold=1
        audio=r.listen(source)
    


    try:
        print("Recognizing..")
        query= r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please..")
        return "None"
    return query
 
def sendEmail(to,contect):
    server =smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('yourname@gamil.com','your-paasword')
    server.sendmail('youremail@gamil.com',to,contect)
    server.close()

if __name__=="__main__":
    speak("sangeeta mishra")
    wishme()

    while True:
        query= takeCommand().lower()

        if 'wikipedia' in query:
            speak('searching Wikipedia..')
            query =query.replace("wikipedia..","")
            result= wikipedia.summary(query,sentences=2)
            speak("Acording Wikipedia")
            print(result)
            speak(result)
        
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open leetcode' in query:
            webbrowser.open('leetcode.com')

        elif 'the time' in query:
            strTime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")
            
        elif 'email to vishal' in query:
            try:
                 speak("What should I say")
                 content=takeCommand()
                 to="aman.vm122005@gamil.com"
                 sendEmail(to,content)
                 speak('Email has been sent!')
            except Exception as e:
                print(e)
                speak("soory my friend vishal bhai. I am not able to send this email")
        