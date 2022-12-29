#Desafio 021 - Faça um programa em python que abra e reproduza o áudio de um arquivo.mp3

import vlc
import time
music = 'MUSICA KIKO.mp3'
player = vlc.MediaPlayer(music)
player.play()
print('Musica está tocando')
time.sleep(179)
print('MUSICA PAROU')