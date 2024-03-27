import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 30
screen = pygame.display.set_mode((1200, 900))
x = 0
y = 0
r = 0
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
score = 0


def new_ball():
    # рисует новый шарик
    global x, y, r
    x = randint(100, 1100)
    y = randint(100, 900)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)


def score_show(score):
    font = pygame.font.Font(None, 100)
    text = font.render(str(score), True, 'White')
    screen.blit(text, (0, 0))


def click(ev, x, y):
    (a, b) = ev.pos
    global score
    if (a - x)**2 + (b-y)**2 > r**2:
        score -= 1


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)

    new_ball()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(event, x, y)
    score_show(score)

    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
