import requests
import wikipedia
import pywhatkit as kit
from email.message import EmailMessage
import smtplib

def get_random_joke():
    headers = {
        'Accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]
