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
status_text = ""


font = pygame.font.SysFont(None, 36)

def update_status(new_status):
    global status_text
    status_text = new_status
    print(new_status)

def play_track():
    global current_track
    pygame.mixer.music.load(tracks[current_track])
    pygame.mixer.music.play()
    track_name = os.path.basename(tracks[current_track])
    update_status(f"Играет: {track_name}")

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
    update_status("Музыка остановлена")

play_track()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Музыкальный плеер")
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN: # вместо pygame.key.get_pressed()
            if event.key == pygame.K_p:
                play_track()
            elif event.key == pygame.K_s:
                stop_music()
            elif event.key == pygame.K_n:
                next_track()
            elif event.key == pygame.K_b:
                previous_track()

    screen.fill("white")

    status_surface = font.render(status_text, True, (0, 0, 0))
    text_rect = status_surface.get_rect(center=(400, 300))
    screen.blit(status_surface, text_rect)
    
    #instructions = "P - Play, S - Stop, N - Next, B - Previous"


    pygame.display.flip()
    clock.tick(60)

pygame.quit()
