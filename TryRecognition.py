import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()


with sr.Microphone() as source:
    print('Escuchando...')
    voice = listener.listen(source)
    command = listener.recognize_google(voice,language='es-MX')
    command = command.lower()
    if 'alexa' in command:
        command = command.replace('alexa', '')
        print(command)
    else:
        print(command)