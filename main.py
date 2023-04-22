import speech_recognition as sr
import pyttsx3
import pywhatkit as kit
import datetime
import pyjokes
import subprocess

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 175)

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
                print(command)

    except:
        pass
    return command


def run_jarvis():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song + ' sir ')
        kit.playonyt(song, use_api=True)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('it is ' + time + ' sir')
        print('it is ' + time + ' sir')
    elif 'open steam' in command:
        subprocess.Popen('C:\Program Files (x86)\Steam\Steam.exe')
        talk('opening sir')
    elif 'open discord' in command:
        subprocess.Popen(r'C:\Users\2007T\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Discord Inc')
        talk('opening sir')
    elif 'open epic games' in command:
        subprocess.Popen('C:\Program Files (x86)\Epic Games\Launcher\Engine\Binaries\Win32\EpicGamesLauncher.exe')
        talk('opening sir')
    elif 'search' in command:
        wikinfo = command.replace('search', '')
        talk('on your way, sir')
        kit.search(wikinfo)
    elif 'tell me about' in command:
        information = command.replace('tell me about', '')
        talk('i found this, sir')
        kit.info(information)
    elif 'send message' in command:
        message = command.replace('send this', '')
        print(message)
        talk('whats the number')
        number = input('whats the number:')
        talk('the hour sir:')
        hour = int(input('the hour:'))
        talk('and the minute')
        minute = int(input('and the minute:'))
        kit.sendwhatmsg(number,message,hour,minute)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'shut down please' in command:
        talk('shutting down')
        kit.shutdown(time=20)
    elif 'cancel the countdown' in command:
        kit.cancelShutdown()
        talk('no worries')
    else:
        talk('please repeat the command')

while True:
    run_jarvis()






























