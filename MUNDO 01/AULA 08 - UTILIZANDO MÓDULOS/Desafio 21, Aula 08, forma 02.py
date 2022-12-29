#Desafio 021 - Faça um programa em python que abra e reproduza o áudio de um arquivo.mp3

#Forma 02 - Utilizando o módulo pygame

import pygame

pygame.mixer.init()
pygame.mixer.music.load('MUSICA KIKO.mp3')
pygame.mixer.music.play()
import time
time.sleep(360)