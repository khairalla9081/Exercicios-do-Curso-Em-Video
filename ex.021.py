import pygame
pygame.mixer.init()
pygame.mixer.music.load('ex.21.mp3')
pygame.mixer.music.play()
while(pygame.mixer.get_busy()):pass
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx