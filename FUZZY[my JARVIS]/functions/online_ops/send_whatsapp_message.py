import requests
import wikipedia
import pywhatkit as kit
from email.message import EmailMessage
import smtplib


def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"+91{number}", message)
