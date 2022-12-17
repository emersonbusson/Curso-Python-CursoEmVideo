import vlc
import time
music = 'MUSICA KIKO.mp3'
player = vlc.MediaPlayer(music)
player.play()
print('Musica está tocando')
time.sleep(179)
print('MUSICA PAROU')

#FAÇA UM PROGRAMA EM PYTHON QUE ABRA E REPRODUZA O ÁUDIO DE UM ARQUIVO.MP3