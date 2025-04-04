import pygame
import random
import time


pygame.init()

WIDTH, HEIGHT = 400, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer")

background = pygame.image.load(r"C:\Users\kafka\Documents\Demo\lab8\r\PygameTutorial_3_0\AnimatedStreet.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
player_img = pygame.image.load(r"C:\Users\kafka\Documents\Demo\lab8\r\PygameTutorial_3_0\Player.png")
enemy_img = pygame.image.load(r"C:\Users\kafka\Documents\Demo\lab8\r\PygameTutorial_3_0\Enemy.png")
coin_img = pygame.image.load(r"C:\Users\kafka\Documents\Demo\lab8\r\coin.png")
super_coin_img = pygame.image.load(r"C:\Users\kafka\Documents\Demo\lab8\r\super_coin.png")

#Set up game variables
SPEED = 5
SCORE = 0
COINS_COLLECTED = 0
LEVEL_UP_COIN_COUNT = 5

#Clock and font
clock = pygame.time.Clock()
font = pygame.font.SysFont("Verdana", 20)

#Define classes
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect(center=(160, 520))

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-5, 0)
        if pressed_keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.move_ip(5, 0)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect(center=(random.randint(40, WIDTH - 40), 0))

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, WIDTH - 40), 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self, is_super=False):
        super().__init__()
        self.is_super = is_super
        self.image = pygame.transform.scale(super_coin_img if is_super else coin_img, (40, 40))
        self.value = 3 if is_super else 1
        self.rect = self.image.get_rect(center=(random.randint(30, WIDTH - 30), 0))

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > HEIGHT:
            self.kill()

#Setup sprite groups
player = Player()
enemy = Enemy()
all_sprites = pygame.sprite.Group()
coins = pygame.sprite.Group()
enemies = pygame.sprite.Group()

all_sprites.add(player)
all_sprites.add(enemy)
enemies.add(enemy)

#Timers for coins and speed increase
ADD_COIN = pygame.USEREVENT + 1
pygame.time.set_timer(ADD_COIN, 1000)

running = True
while running:
    win.fill((0, 0, 0))  # Clear screen
    win.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == ADD_COIN:
            if len(coins) == 0:  #Only spawn new coin if no coins exist
                is_super = random.random() < 0.2  #20% chance for super coin
                new_coin = Coin(is_super)
                all_sprites.add(new_coin)
                coins.add(new_coin)

    #Move and draw all sprites
    for entity in all_sprites:
        entity.move()
        win.blit(entity.image, entity.rect)

    player.move()

    #Check collision with coins
    collided_coin = pygame.sprite.spritecollideany(player, coins)
    if collided_coin:
        COINS_COLLECTED += collided_coin.value
        collided_coin.kill()

        #Increase speed after every N coins
        if COINS_COLLECTED % LEVEL_UP_COIN_COUNT == 0:
            SPEED += 1

    #Check collision with enemy
    if pygame.sprite.spritecollideany(player, enemies):
        pygame.mixer.Sound(r"C:\Users\kafka\Documents\Demo\lab8\r\PygameTutorial_3_0\crash.wav").play()
        time.sleep(1)
        win.fill((255, 0, 0))  #Game Over
        text = font.render("Game Over", True, (0, 0, 0))
        win.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2))
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        exit()

    #Display score and coin count
    score_text = font.render(f"Score: {SCORE}", True, (255, 255, 255))
    coin_text = font.render(f"Coins: {COINS_COLLECTED}", True, (255, 255, 0))
    win.blit(score_text, (10, 10))
    win.blit(coin_text, (10, 40))

    pygame.display.update()
    clock.tick(60)  #60 FPS
