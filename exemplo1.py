import pyttsx3

engine = pyttsx3.init()

engine.setProperty('volume', 1.0)

for rate in range(60, 261, 20):
    engine.setProperty('rate', rate)
    engine.say("Good Morning!")
    engine.runAndWait()
