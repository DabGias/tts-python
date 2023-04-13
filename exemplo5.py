from gtts import gTTS
from pygame import mixer
import os

diret = input("Digite o caminho do arquivo: ")

if os.path.isfile(diret):
    print("Carregando o arquivo! Aguarde...")

    with open(diret, encoding="utf-8") as file:
        texto = file.read()

        print(texto)
        print("Efetuando leitura do arquivo...")

        mp3 = gTTS(texto, lang='pt')

        print("Salvando o arquivo de áudio...")

        mp3.save("afazeres.mp3")

        print("Falando...")

        mixer.init()
        mixer.music.load("afazeres.mp3")
        mixer.music.play()

        input("Aperte enter para finalizar!")
else:
    print("Arquivo inexistente!")
