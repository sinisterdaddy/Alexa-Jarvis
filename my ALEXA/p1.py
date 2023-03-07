import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer ()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[2].id)  # Selected Brian Voice (third party)
def talk(text) :
    engine.say(text)
    engine.runAndWait() 

def take_command ( ) :
    try:
         with sr.Microphone() as source :
             print("listening....")
             voice =listener.listen(source)
             command = listener.recognize_google(voice)
             command = command.lower()
             if "" in command:
                 command = command.replace('replace' , " " )
                 print(command)
    except:
        pass
    return command

def run_():
        command = take_command()
        print(command)
        if "play" in command :
           song = command.replace ("play", " ")
           talk('playing song')
           pywhatkit.playonyt(song)
        elif 'time' in command :
            time = datetime.datetime.now().strftime("%I:%M %p")     
            talk ("current time is"+time)
        elif 'who the heck is ' in command:
            person = command.replace('who the heck is' , ' ') 
             
        elif 'date' in command:
            talk("sorry i have a headache")
        elif "are you single" in command :
            talk("belive me you would be last person on earth with whom i would go on a date with")
        elif "joke" in command:
            talk(pyjokes.get_joke())
        else:
            talk("please say the command again")
while True:
    run_()
        
        
        

    
    
    
