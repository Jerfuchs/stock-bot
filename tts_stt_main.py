import speech_recognition as sr
import pyttsx3
from google_trans_new import google_translator
from gtts import gTTS
import playsound
from programy.clients.embed.datafile import EmbeddedDataFileBot
from config.config import *

translator = google_translator()
stock_bot = EmbeddedDataFileBot(files, defaults=True)  # Bot initialised/ Extend to Stock Bot
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
# engine.setProperty("voice", voices[7].id) #Die klassische Stimme
#engine.setProperty("voice", voices[11].id) #Stephen Hawking
engine.setProperty("voice", voices[4].id) #Default (Deutsch)
#engine.setProperty("voice", voices[0].id) #Default (Englisch)


def talk(text):
    response = stock_bot.ask_question(text)
    # my_bot.wait_and_answer()
    response = translator.translate(response,lang_src="en",lang_tgt="de")
    if(str(response) != "None"):
        engine.say(response)
        print("Bot: ", response)
        engine.runAndWait()
    else:
        fallback()


def get_command():
    command = ""
    try:
        with sr.Microphone() as source:
            print("Listening....")
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language='de-DE')
            print("User: ", command)
            command = translator.translate(str(command),lang_src="de",lang_tgt="en")
    except Exception as e:
        print(str(e))
        fallback()
    return command

def fallback():
    engine.say("Ich habe Ihre Anfrage nicht verstanden! Können Sie sich wiederholen?")
    engine.runAndWait()


def runStockBot():
    talk(get_command())

engine.say("Hi, mein Name ist StockBot! Was kann ich für Sie tun?")
engine.runAndWait()

while True:
    runStockBot()
