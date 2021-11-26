import pygame as p
from pygame.draw import *
from random import randint
p.init()
# VARIABLES
ping = 10
score = 0

# COLORS
red = (255, 0, 0)
blu = (0, 0, 255)
yw = (255, 255, 0)
gr = (0, 255, 0)
pi = (255, 0, 255)
cyan = (0, 255, 255)
bl = (0, 0, 0)
me = (240, 255, 240)
mel = (255, 250, 205)
sky = (0, 191, 255)
lpi = (218, 112, 214)
ora = (255, 140, 0)
w = (255, 255, 255)
COLORS = [red, blu, yw, gr, pi, cyan, bl, me, mel, sky, lpi, ora, w]

screen = p.display.set_mode((1200, 900))


# balls
class Ball:
    def __init__(self):
        self.x = randint(100, 1100)
        self.y = randint(100, 900)
        self.r = randint(10, 100)
        self.dx = 5
        self.dy = 5
        self.color = COLORS[randint(0, 12)]

    def show(self):
        circle(screen, self.color, (self.x, self.y), self.r)

    def change_location(self):
        self.x += self.dx
        self.y += self.dy
        if self.x >= 1200 - self.r or self.x <= self.r:
            self.dx *= -1
        if self.y >= 900 - self.r or self.y <= self.r:
            self.dy *= -1
        self.show()


# score
def score_show(score):
    font = p.font.Font(None, 100)
    text = font.render(str(score), True, w)
    screen.blit(text, (0, 0))


def score_change(ev):
    global score
    (x, y) = ev.pos
    if (a.x - x)**2 + (a.y - y)**2 <= a.r**2:
        score += 1





# DISPLAY
a = Ball()
a.show()

########################################################
p.display.update()
clock = p.time.Clock()
finished = False

while not finished:
    clock.tick(ping)
    screen.fill(bl)
    score_show(score)
    a.change_location()

    for event in p.event.get():
        if event.type == p.QUIT:
            finished = True
        elif event.type == p.MOUSEBUTTONDOWN:
            score_change(event)

    p.display.update()



p.quit()
