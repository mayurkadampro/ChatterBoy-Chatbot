from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

def setup():
    chatbot = ChatBot('Bot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    trainer='chatterbot.trainers.ListTrainer')
    convData = open("greetings.yml",'r',encoding="utf-8").readlines()
    chatbot.set_trainer(ListTrainer)
    chatbot.train(convData)
    print("Training Completed")
    

setup()
