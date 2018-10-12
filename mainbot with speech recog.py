from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
import pyttsx3
import speech_recognition as sr
import sys
import os

BLUE = '\33[94m'
LightBlue = '\033[94m'
RED = '\033[91m'
WHITE = '\33[97m'
YELLOW = '\33[93m'
GREEN = '\033[32m'
LightCyan    = "\033[96m"
END = '\033[0m'


if len(sys.argv) < 2:
    os.system("clear || cls")
    sys.stdout.write(RED + """

         ██████╗██╗  ██╗ █████╗ ████████╗████████╗███████╗██████╗     ██████╗  ██████╗ ██╗   ██╗
        ██╔════╝██║  ██║██╔══██╗╚══██╔══╝╚══██╔══╝██╔════╝██╔══██╗    ██╔══██╗██╔═══██╗╚██╗ ██╔╝
        ██║     ███████║███████║   ██║      ██║   █████╗  ██████╔╝    ██████╔╝██║   ██║ ╚████╔╝ 
        ██║     ██╔══██║██╔══██║   ██║      ██║   ██╔══╝  ██╔══██╗    ██╔══██╗██║   ██║  ╚██╔╝  
        ╚██████╗██║  ██║██║  ██║   ██║      ██║   ███████╗██║  ██║    ██████╔╝╚██████╔╝   ██║   
         ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚══════╝╚═╝  ╚═╝    ╚═════╝  ╚═════╝    ╚═╝   
                                                                                        
     
    """)
else:
    sys.exit('Usage: python G-Bomber.py')
    os.system("clear || cls")

print(END)


bot = ChatBot('Bot', storage_adapter='chatterbot.storage.SQLStorageAdapter',
logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch'
        },
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.2,
            'default_response': 'I am sorry, but I do not understand.'
        }
    ],trainers='chatterbot.trainers.ListTrainers')
bot.set_trainer(ListTrainer)

r=sr.Recognizer()
r.pause_threshold = 2
r.enery_threshold = 400
x=pyttsx3.init()
x.setProperty('rate',130)
x.setProperty('volume',8)

while True:
    with sr.Microphone() as source:
        try:
            print(LightCyan+'[?] '+YELLOW+" Say Someting I'm listning now.........."+END)
            audio = r.listen(source, timeout=5)
            print()
            message = r.recognize_google(audio)
        except LookupError:
            print(LightCyan+'[x] '+YELLOW+' Could Not Understand'+END)
            break
        except sr.UnknownValueError:
            print(LightCyan+'[x] '+YELLOW+' You are not speaking........'+END)
            break
        except KeyboardInterrupt:
            print(LightCyan+'[x] '+YELLOW+' Canceled....'+END)

    print(LightCyan+'[?] '+YELLOW+" Human : "+END,RED+"",message,""+END)
    if message.strip()=="Bye" or message.strip()=="bye":
        bye = "Bye Have A Nice Day!"
        print(LightCyan+'[+] '+YELLOW+" ChatterBoy : "+END,RED+"",bye,""+END)
        x.say(bye)
        x.runAndWait()
        break
    if message.strip() != "Bye":
        x.say(message)
        x.runAndWait()
        reply=bot.get_response(message)
        print(LightCyan+'[+] '+YELLOW+" ChatterBoy : "+END,RED+"",reply,""+END)
        x.say(reply)
        x.runAndWait()
        print()     
        
