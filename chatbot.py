import pyttsx3
import datetime
import wikipedia
import smtplib
import webbrowser
import speech_recognition as sr
import urllib.request
import urllib.parse
import re
import pytube
import os
class bot:
    def speak(self, user):
        self.engine = pyttsx3.init()
        self.speech = self.engine.say(user)
        self.engine.runAndWait()
    def return_wiki(self, a):
        return wikipedia.summary(a)
    def __init__(self): 
        
        time = datetime.datetime.now().hour
        if time < 12 and time >= 0 :
            self.speak('Good Morning Sir')
        elif time >= 12 and time < 18:
            self.speak('Good Afternoon Sir')
        elif time >= 18 :
            self.speak('good Evening Sir')         
        self.speech_recog()
    def openwebsite(self, website_name):             
        webbrowser.open('www.'+ website_name+'.com')  
    def play_song(self, name):
        query_string = urllib.parse.urlencode({"search_query" : name})
        html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
        search_results = re.findall(r'/watch\?v=(.{11})', html_content.read().decode())
        input2 = "http://www.youtube.com/watch?v=" + search_results[0]
        video = pytube.YouTube(input2)
        video.streams.first().download(filename='file')
        os.startfile('file.mp4')
    def send_email(self, email, password, target_email,email_content, subject):
        self.msg = f"subject:{subject}\n\n\n{email_content}"
        with smtplib.SMTP('smtp.gmail.com',587) as self.server :
            self.server.starttls()
            self.server.login(email, password)
            self.server.sendmail(email,target_email, self.msg)
            self.server.quit()
    def speech_recog_again(self, msg):
        mic = sr.Recognizer()
        self.speak(msg)
        with sr.Microphone() as self.source:
            mic.pause_threshold = 1
            self.audio = mic.listen(self.source)
        try:
            self.speak('recognising.....')
            query = mic.recognize_google(self.audio, language='en-in').lower() 
            print(query)
            self.speak('recognised......')
            return query
        except:
            self.speak('try' + msg + 'again')
            self.speech_recog_again(msg)
    def speech_recog(self):
        mic = sr.Recognizer()
        self.speak('how may i help you?')
        with sr.Microphone() as self.source:
            mic.pause_threshold = 1
            self.audio = mic.listen(self.source)
        try:
            self.speak('recognised......')
            query = mic.recognize_google(self.audio, language='en-in').lower() 
            self.speak('recognised......')
            if ("open" in query):
                site = self.speech_recog_again("enter site name")
                self.openwebsite(site)
            elif ('song' in query):
                song_name = self.speech_recog_again('enter song name')
                self.play_song(song_name)
            elif ('wiki' in query or 'wikipedia' in query):
                try:  
                    item = self.speech_recog_again('what topic do u want to search?')
                    self.speak('note if this gives an error that means that wikipedia is returning an error u can try again or search a diffrent topic')
                    a= self.return_wiki(item)
                    print(a)
                    self.speak(a)
                except:
                    self.speech('info not avabilable pls try again on an diffrent topic')
            elif ('email' in query or 'e mail' in query or "mail" in query):
                self.speak('processing request')
                self.email_input_requests()
            elif ('quit' in query):
                self.speak('quitting. have a good day')
            else:
                self.speak('try again invalid command')
                self.speech_recog()
        except:
            self.speak('retrying')
            self.speech_recog()
    def email_input_requests(self):
        self.speak('please note we can only take gmail as your email and the password shuld be real. less secure app access should be true')
        self.speak('you will have to type the feilds for better accuracy')
        self.speak('..enter your email')
        self.a = input()
        self.speak('..enter your email\'s password')
        self.b =input()
        self.speak('..enter receiver\'s email')
        self.c = input()
        self.speak('enter subject')
        self.d= input()
        self.speak('enter the body of the message')
        self.e = input()
        self.send_email(self.a, self.b, self.c,self.e,self.d)
        self.speech_recog()
bot = bot()