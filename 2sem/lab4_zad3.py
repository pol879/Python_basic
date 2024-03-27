import pygame as pg
from pygame.draw import *
from random import *

pg.init()
ping = 30
d = 40
clock = pg.time.Clock()
# COLORS:
bb = (110, 100, 80)
bl = (0, 0, 0)
w = (255, 255, 255)
br = (150, 75, 0)

sc = pg.display.set_mode((794, 1050))
sc.fill((95, 189, 221))  # sky
rect(sc, (50, 200, 110), (0, 542, 794, 1123))  # grass


# FENCE begins here
def fence_normal(x, y, kw, kh, k):
    width = int(794*kw)
    height = int(350*kh)
    fence_surface = pg.Surface((width, height))
    fence_surface.fill((200, 170, 50))
    X = 0
    d = 40*k
    line(fence_surface, (152, 156, 153), (0, 0), (width, 0), 1)
    line(fence_surface, (0, 0, 0), (0, height - 1), (width, height - 1), 1)
    line(fence_surface, (0, 0, 0), (width - 1, 0), (width - 1, height), 1)
    for i in range(1100 // 40):
        line(fence_surface, (0, 0, 0), (X, 0), (X, height), 1)
        X += d
    sc.blit(fence_surface, (x, y))


small_width = 436/794
small_height = 267/350
fence_normal(154, 14, 1, 392/350, 1.5)
fence_normal(0, 277, small_width, small_height, 1)
fence_normal(-70, 436, small_width, small_height, 1)
fence_normal(395, 405, small_width, small_height, 1)
# FENCE ends here

ds = pg.Surface((234, 175))
ds.fill((95, 150, 200))
ds.set_colorkey((95, 150, 200))
# DOG starts here
# BODY
ellipse(ds, bb, (55, 40, 145, 80))
ellipse(ds, bb, (135, 35, 50, 60))
ellipse(ds, bb, (145, 38, 80, 60))
ellipse(ds, bb, (180, 70, 55, 60))
ellipse(ds, bb, (220, 110, 15, 50))
ellipse(ds, bb, (160, 90, 15, 50))
ellipse(ds, bb, (130, 130, 40, 15))
ellipse(ds, bb, (190, 150, 40, 15))
ellipse(ds, bb, (85, 90, 40, 80))
ellipse(ds, bb, (25, 70, 40, 80))
ellipse(ds, bb, (5, 140, 40, 15))
ellipse(ds, bb, (65, 160, 40, 15))
# HEAD starts here
rect(ds, bb, (10, 0, 80, 80))
rect(ds, bl, (10, 0, 80, 80), 2)
# EARS
ellipse(ds, bb, (0, 0, 25, 30))
ellipse(ds, bl, (0, 0, 25, 30), 2)
ellipse(ds, bb, (80, 0, 25, 30))
ellipse(ds, bl, (80, 0, 25, 30), 2)
# EYES
ellipse(ds, w, (27, 30, 20, 8))
ellipse(ds, bl, (27, 30, 20, 8), 2)
ellipse(ds, w, (57, 30, 20, 8))
ellipse(ds, bl, (57, 30, 20, 8), 2)
circle(ds, bl, (36, 34), 4)
circle(ds, bl, (66, 34), 4)
# MOUTH
# smile
ellipse(ds, bl, (30, 59, 40, 15), 2)
rect(ds, bb, (30, 59, 40, 8))
# teeth
polygon(ds, w, [(35, 69), (40, 64), (42, 72)])
polygon(ds, bl, [(35, 69), (40, 64), (42, 72)], 2)
polygon(ds, w, [(65, 69), (60, 64), (58, 72)])
polygon(ds, bl, [(65, 69), (60, 64), (58, 72)], 2)
# NOSE
ellipse(ds, (139, 58, 58), (43, 50, 15, 8))
ellipse(ds, bl, (43, 50, 15, 8), 2)
# HEAD ends here
# DOG ends here

# dogs display:
ds_mirror = pg.transform.flip(ds, True, False)
sc.blit(pg.transform.scale(ds, (284, 255)), (40, 510))
sc.blit(pg.transform.scale(ds_mirror, (284, 255)), (40, 760))
sc.blit(pg.transform.scale(ds_mirror, (206, 147)), (570, 636))

# DOGHOUSE
# building
dx = 123
dy = 160
polygon(sc, br, [(380 + dx, 515 + dy), (485 + dx, 540 + dy), (485 + dx, 675 + dy), (380 + dx, 625 + dy)])
polygon(sc, bl, [(380 + dx, 515 + dy), (485 + dx, 540 + dy), (485 + dx, 675 + dy), (380 + dx, 625 + dy)], 2)
polygon(sc, br, [(485 + dx, 675 + dy), (485 + dx, 540 + dy), (520 + dx, 510 + dy), (520 + dx, 606 + dy)])
polygon(sc, bl, [(485 + dx, 675 + dy), (485 + dx, 540 + dy), (520 + dx, 510 + dy), (520 + dx, 606 + dy)], 2)
polygon(sc, br, [(380 + dx, 515 + dy), (435 + dx, 440 + dy), (485 + dx, 540 + dy)])
polygon(sc, bl, [(380 + dx, 515 + dy), (435 + dx, 440 + dy), (485 + dx, 540 + dy)], 2)
polygon(sc, br, [(485 + dx, 540 + dy), (520 + dx, 510 + dy), (475 + dx, 425 + dy), (435 + dx, 440 + dy)])
polygon(sc, bl, [(485 + dx, 540 + dy), (520 + dx, 510 + dy), (475 + dx, 425 + dy), (435 + dx, 440 + dy)], 2)
ellipse(sc, bl, (400 + dx, 550 + dy, 50, 70))
circle(sc, bl, (395 + dx, 620 + dy), 5)

# chain
x0, y0 = 395 + dx, 610 + dy
delx, dely = randint(1, 10), randint(1, 10)
ellipse(sc, (100, 100, 100), (x0, y0, delx, dely), 2)
for i in range(10):
    delx, dely = randint(6, 10), randint(1, 10)
    x0 -= delx
    y0 += dely * ((-1) ** i)
    ellipse(sc, (100, 100, 100), (x0, y0, delx + 10, dely + 10), 2)
# bone
rect(sc, w, (x0, y0, 15, 5))
circle(sc, w, (x0, y0), 3)
circle(sc, w, (x0 + 15, y0), 3)
circle(sc, w, (x0, y0 + 5), 3)
circle(sc, w, (x0 + 15, y0 + 5), 3)

# dog - display bottom_right corner:
sc.blit(pg.transform.scale(ds, (634, 535)), (500, 750))


# END OF DRAWING

pg.display.update()
finished = False

while not finished:
    clock.tick(ping)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True
pg.quit()
