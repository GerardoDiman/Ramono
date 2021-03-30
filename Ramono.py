import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
listener.energy_threshold = 3000 # Nivel de energia de los sonidos (type: float)
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('Escuchando...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice,language='es-MX' and 'en-US')
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa','')
                #print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'reproduce' in command:
        song = command.replace('reproduce','')
        talk('reproduciendo ' + song)
        pywhatkit.playonyt(song)
    elif 'hora' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('La hora exacta es: ' + time)
    elif 'Que es' in command:
        person = command.replace('Que es', '')
        info = wikipedia.summary(person,1)
        print(info)
        talk(info)
    elif 'quien es' in command:
        person = command.replace('quien es', '')
        info = wikipedia.summary(person,1)
        print(info)
        talk(info)
    elif 'cual es tu nombre' in command:
        talk('Mi nombre es Alexa')
    elif 'chiste' in command:
        talk(pyjokes.get_joke(spanish))
    elif 'detente' in command:
        exit(0)
    else:
        talk('Repite en comando de nuevo.')



while True:
    run_alexa()