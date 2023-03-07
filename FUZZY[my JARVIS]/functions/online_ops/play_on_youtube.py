import requests
import wikipedia
import pywhatkit as kit
from email.message import EmailMessage
import smtplib

def play_on_youtube(video):
    kit.playonyt(video)
