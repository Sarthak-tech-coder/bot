import sys
import subprocess

def install(name):
  subprocess.check_call([sys.executable, '-m', 'pip', 'install', name])
 install('pyttsx3')
 install('wikipedia')
 install('smtplib')
 
 install('speech_recognition')
 install('pytube')
 install('re')
 install('datetime')
 install('datetime')
