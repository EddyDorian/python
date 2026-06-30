import pygame

pygame.mixer.init()
pygame.mixer.music.load('/home/eddy/Documentos/arquivos/Ana Castela - Chicletinho (Ao Vivo).mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pass