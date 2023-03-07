import requests
import wikipedia
import pywhatkit as kit
from email.message import EmailMessage
import smtplib
def search_on_google(query):
    kit.search(query)
