import requests
import wikipedia
import pywhatkit as kit
from email.message import EmailMessage
import smtplib


def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]
