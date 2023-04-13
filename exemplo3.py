import calendar
from datetime import datetime as dtt
import pyttsx3

nome = input("Digite seu nome: ").strip()
eng = pyttsx3.init()

eng.setProperty('volume', 1.0)
eng.setProperty('rate', 140)

eng.say("Hello {}! It's {} {} of {} {} {}".format(
    nome,
    dtt.now().hour,
    dtt.now().minute,
    calendar.month_name[dtt.today().month],
    dtt.today().day,
    dtt.today().year
))
eng.runAndWait()
