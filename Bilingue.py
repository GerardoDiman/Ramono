import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
listener.energy_threshold = 300 # Nivel de energia de los sonidos (type: float)
recognizer_instance.pause_threshold = 0.8 # Dureación minima de silencio
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
            command = listener.recognize_google(voice,language='es-MX')
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa','')
                print(command)

                command = command
                print(command)
                if 'reproduce' in command:
                    song = command.replace('reproduce', '')
                    talk('reproduciendo ' + song)
                    pywhatkit.playonyt(song)
                elif 'hora' in command:
                    time = datetime.datetime.now().strftime('%I:%M %p')
                    talk('La hora exacta es: ' + time)
                elif 'Que es' in command:
                    person = command.replace('Que es', '')
                    info = wikipedia.summary(person, 1)
                    print(info)
                    talk(info)
                elif 'quien es' in command:
                    person = command.replace('quien es', '')
                    info = wikipedia.summary(person, 1)
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
    except:
        return



while True:
    take_command()