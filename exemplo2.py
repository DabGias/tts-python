from datetime import datetime as dtt
import pyttsx3

agora = dtt.now()
hora = agora.hour
minuto = agora.minute

dia = dtt.today().day
mes = dtt.today().month
ano = dtt.today().year

en = pyttsx3.init()

en.setProperty('volume', 1.0)
en.setProperty('rate', 140)

en.say("It's {} and {}. {} {} {}".format(hora, minuto, mes, dia, ano))
en.runAndWait()
