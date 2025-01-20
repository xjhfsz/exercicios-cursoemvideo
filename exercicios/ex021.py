import pygame
import time

pygame.init()  # inicia o pygame

pygame.mixer.music.load('ex021.mp3')  # carrega o arquivo mp3
pygame.mixer.music.play()  # reproduz o arquivo mp3

# versão windows
pygame.event.wait()  # aguarda o fim da musica

# # versão linux
# while pygame.mixer.music.get_busy():  # aguarda o fim da música
#     time.sleep(1)

