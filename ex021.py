import pygame

# Inicializar o mixer do pygame
pygame.mixer.init()

# Carregar um arquivo MP3
pygame.mixer.music.load("Audio.mp3")

# Tocar o arquivo MP3
pygame.mixer.music.play()

# Manter o script rodando até que a música termine
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
