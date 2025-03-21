import pygame
import os

pygame.init()
pygame.mixer.init()
tracks = [
    r'c:\Users\kafka\Documents\Demo\lab7\player\Lacrimosa.mp3',
    r'c:\Users\kafka\Documents\Demo\lab7\player\Forever And Ever.mp3',
    r'c:\Users\kafka\Documents\Demo\lab7\player\Doktorspiele.mp3'
]

current_track = 0

def play_track():
    pygame.mixer.music.load(tracks[current_track])
    pygame.mixer.music.play()
    print(f"Играет: {tracks[current_track]}")

def next_track():
    global current_track
    current_track = (current_track + 1) % len(tracks)
    play_track()

def previous_track():
    global current_track
    current_track = (current_track - 1) % len(tracks)
    play_track()

def stop_music():
    pygame.mixer.music.stop()
    print("Музыка остановлена")

play_track()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_p]:
        play_track()
    if keys[pygame.K_s]:
        stop_music()
    if keys[pygame.K_n]: 
        next_track()
    if keys[pygame.K_b]:
        previous_track()

    screen.fill("white")
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
