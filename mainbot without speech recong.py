from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import pyttsx3
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
    sys.exit('Usage: python mainbot.py')
    os.system("clear || cls")

print(END)


def bot():
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

 
    x=pyttsx3.init()
    x.setProperty('rate',130)
    x.setProperty('volume',8)
    while (True):
        msg = input(LightCyan+'[?] '+YELLOW+" Human : "+RED)
        if msg.strip() == 'Bye' or msg.strip() == 'bye':
            x.say(msg)
            bye='Bye & Have a nice day !!!!!'
            print(LightCyan+'[?] '+YELLOW+" ChatterBoy :"+END,RED+"",bye,""+END)
            x.say(bye)
            x.runAndWait()
            break
        if msg.strip() != 'Bye':
            x.say(msg)
            reply = bot.get_response(msg)
            print(LightCyan+'[?] '+YELLOW+" ChatterBoy : "+END,RED+"",reply,""+END)
            x.say(reply)
            x.runAndWait()
            print()
        
bot()        
        
