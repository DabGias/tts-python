from gtts import gTTS
from pygame import mixer

mp3 = gTTS("Amanhã é sexta feira!", lang='pt')

mp3.save("sexta.mp3")

mixer.init()
mixer.music.load("sexta.mp3")
mixer.music.play()

input("Aperte enter para encerrar!")
