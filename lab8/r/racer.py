import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

#цвета
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#размеры экрана и скорость объектов
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINS = 0  #счетчик монет

#шрифты
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

#фон
background = pygame.image.load(r"C:\Users\kafka\Documents\Demo\lab8\r\PygameTutorial_3_0\AnimatedStreet.png")

#окно
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

#враг
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(r"C:\Users\kafka\Documents\Demo\lab8\r\PygameTutorial_3_0\Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.bottom > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

#игрок
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(r"C:\Users\kafka\Documents\Demo\lab8\r\PygameTutorial_3_0\Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

#монетка
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        original_image = pygame.image.load(r"C:\Users\kafka\Documents\Demo\lab8\r\coin.png")
        #масштабируем
        self.image = pygame.transform.scale(original_image, (30, 30))
        self.rect = self.image.get_rect()
        #случайная позиция
        self.rect.center = (random.randint(30, SCREEN_WIDTH - 30), 0)

    def move(self):
        self.rect.move_ip(0, SPEED)
        #если монета уходит за экран -появляется заново сверху
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(30, SCREEN_WIDTH - 30), 0)

#игровые объекты
P1 = Player()
E1 = Enemy()
C1 = Coin()

#sprites
enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()
coins.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

# Создаем пользовательское событие увеличения скорости
#INC_SPEED = pygame.USEREVENT + 1
           #pygame.time.set_timer(INC_SPEED, 1000)

#главный игровой цикл
while True:
    for event in pygame.event.get():



        #if event.type == INC_SPEED:
            #SPEED += 0.5  



        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #отрисовка фона
    DISPLAYSURF.blit(background, (0, 0))

    #отображение счета (очки за уклонение)
    scores = font_small.render("Score: " + str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))

    #отображение количества монет
    coin_score = font_small.render("Coins: " + str(COINS), True, BLACK)
    DISPLAYSURF.blit(coin_score, (SCREEN_WIDTH - 100, 10))

    #движение и отрисовка всех объектов
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)

    #game over при столкновении
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound(r"C:\Users\kafka\Documents\Demo\lab8\r\PygameTutorial_3_0\crash.wav").play()
        time.sleep(1)

        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    #сбор монетки
    if pygame.sprite.spritecollideany(P1, coins):
        COINS += 1
        for coin in coins:
            coin.rect.top = 0
            coin.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    #oбновление экрана и ожидание следующего кадра
    pygame.display.update()
    FramePerSec.tick(FPS)
