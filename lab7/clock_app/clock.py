import pygame
import datetime

pygame.init()

WIDTH, HEIGHT = 600, 600
CENTER = (WIDTH // 2, HEIGHT // 2)

b0dy = pygame.image.load(r"C:\Users\kafka\Documents\Demo\lab7\clock_app\body.png")
min_hand = pygame.image.load(r"C:\Users\kafka\Documents\Demo\lab7\clock_app\min_hand.png")
sec_hand = pygame.image.load(r"C:\Users\kafka\Documents\Demo\lab7\clock_app\sec_hand.png")


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey_Mouse_clock")

clock = pygame.time.Clock()

running = True
while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    now = datetime.datetime.now()
    minutes = now.minute
    seconds = now.second


    minute_angle = -(minutes % 60) * 6 
    second_angle = -(seconds % 60) * 6 

    rotated_right_hand = pygame.transform.rotate(min_hand, minute_angle)
    rotated_left_hand = pygame.transform.rotate(sec_hand, second_angle)

    right_hand_rect = rotated_right_hand.get_rect(center=CENTER)
    left_hand_rect = rotated_left_hand.get_rect(center=CENTER)

    screen.blit(b0dy, (-100, 0))
    screen.blit(rotated_right_hand, right_hand_rect)
    screen.blit(rotated_left_hand, left_hand_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
