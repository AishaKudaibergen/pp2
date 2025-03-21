import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('red circle')
done = False

clock = pygame.time.Clock()

white = (255, 255, 255)
red = (255, 0, 0)

radius = 25
speed = 20 
x, y = WIDTH // 2, HEIGHT // 2

while not done:
    screen.fill(white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]: 
        x = max(radius, x - speed)  
    if pressed[pygame.K_RIGHT]: 
        x = min(WIDTH - radius, x + speed)  
    if pressed[pygame.K_UP]: 
        y = max(radius, y - speed)  
    if pressed[pygame.K_DOWN]: 
        y = min(HEIGHT - radius, y + speed)

    pygame.draw.circle(screen, red, (x,y), radius)
    
    clock.tick(50)        
    pygame.display.flip()

pygame.quit()
    