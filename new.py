import pygame as p
from pygame.draw import *
from random import randint

p.init()
ping = 60
score = 0
n = 1
c = 1
k = 1
a = []
clock = p.time.Clock()
# COLORS
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (0, 250, 154)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
ME = (240, 255, 240)
MEL = (255, 250, 205)
SKY = (0, 191, 255)
PINK = (218, 112, 214)
ORANGE = (255, 140, 0)
COLORS = [BLUE, YELLOW, GREEN, MAGENTA, CYAN, ME, SKY, PINK, MEL, ORANGE]

screen = p.display.set_mode((1200, 900))
p.display.update()
finished = False


class Ball:
    def __init__(self):
        self.x = randint(100, 1100)
        self.y = randint(100, 900)
        self.r = randint(10, 100)
        self.dx = 2
        self.dy = 2
        self.color = COLORS[randint(0, 9)]

    def show(self):
        circle(screen, self.color, (self.x, self.y), self.r)

    def change_location(self):
        self.x += self.dx
        self.y += self.dy
        if self.x >= 1200 - self.r or self.x <= self.r:
            self.dx *= -1
        if self.y >= 900 - self.r or self.y <= self.r:
            self.dy *= -1


def new_ball(n):
    for i in range(n):
        a.append(c)
    for j in range(n):
        a[j] = Ball()
        a[j].show()


def move_ball(n):
    for i in range(n):
        a[i].change_location()
        a[i].show()


def click(ev, n):
    (x, y) = ev.pos
    global score
    for i in range(n):
        if (a[i].x - x)**2 + (a[i].y - y)**2 <= a[i].r**2:
            score += 1


def score_show(score):
    rect = p.Rect(0, 0, 40, 60)
    font = p.font.Font(None, 100)
    text = font.render(str(score), True, WHITE)
    p.draw.rect(screen, BLACK, rect)
    screen.blit(text, (0, 0))


while not finished:
    clock.tick(ping)

    k = n
    new_ball(n)
    move_ball(n)

    for event in p.event.get():
        if event.type == p.QUIT:
            finished = True
        elif event.type == p.MOUSEBUTTONDOWN:
            click(event, k)
    score_show(score)

    n += 1

    p.display.update()



p.quit()
