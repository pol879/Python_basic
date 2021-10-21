import pygame as p
import math
grad = math.pi / 180
beta = 0
p.init()


def regular_polygon(surf, color, n, angle, x, y, r):
    pts = []
    for i in range(n):
        x = x + r * math.cos(angle + math.pi * 2 * i / n)
        y = y + r * math.sin(angle + math.pi * 2 * i / n)
        pts.append([x, y])
    p.draw.polygon(surf, color, pts)
    p.draw.polygon(surf, 'Black', pts, 1)
# x, y - координаты левой верхней вершины многоугольника
# angle - угол поворота многоугольника: по часовой стрелке


def double_regular_polygon(surf, color, n, alpha, x, y, r):
    regular_polygon(surf, color, n, alpha + 180*grad, x, y, r)
    angle_inside = (180 * (n - 2) / n) * grad
    global beta
    beta = 180 * grad - alpha - angle_inside
    regular_polygon(surf, color, n, 180*grad + beta, 900 - x, y, r)


FPS = 30

screen = p.display.set_mode((927, 769))
surface = p.Surface((927, 769))
surface.fill((230, 230, 230))

# TEXT
font = p.font.Font(None, 127)
text_surf = font.render('PYTHON is AMAZING', True, (0, 0, 0))
text_rect = text_surf.get_rect(topleft=(0, 0))


# display
screen.blit(surface, (0, 0))

# body
p.draw.circle(screen, (255, 102, 0), (450, 769), 244)
p.draw.circle(screen, (233, 198, 175), (450, 402), 228)
p.draw.line(screen, (233, 198, 175), (82, 118), (240, 608), 60)
p.draw.ellipse(screen, (233, 198, 175), (39, 47, 86, 86))
p.draw.ellipse(screen, 'white', (39, 47, 86, 86), 1)

p.draw.line(screen, (233, 198, 175), (818, 118), (660, 608), 60)
p.draw.ellipse(screen, (233, 198, 175), (775, 47, 86, 86))
p.draw.ellipse(screen, 'white', (775, 47, 86, 86), 1)
regular_polygon(screen, (255, 102, 0), 5, math.pi/4, 256, 531, 100)
regular_polygon(screen, (255, 102, 0), 5, 27*grad, 644, 531, 100)

# text_display
p.draw.rect(screen, (127, 255, 42), text_rect)
screen.blit(screen, text_rect)
screen.blit(text_surf, (0, 0))
p.draw.rect(screen, 'Black', text_rect, 1)

# NOSE
p.draw.polygon(screen, (120, 68, 33), [(430, 415), (470, 415), (450, 415+20*math.sqrt(3))])
p.draw.polygon(screen, 'Black', [(430, 415), (470, 415), (450, 415+20*math.sqrt(3))], 1)

# MOUTH
p.draw.polygon(screen, (255, 42, 42), [(330, 475), (570, 475), (450, 550)])
p.draw.polygon(screen, 'Black', [(330, 475), (570, 475), (450, 550)], 1)

# EYES
p.draw.ellipse(screen, (128, 179, 255), (330, 318, 86, 76))
p.draw.ellipse(screen, 'Black', (330, 318, 86, 76), 1)
p.draw.circle(screen, 'Black', (373, 356), 12)

p.draw.ellipse(screen, (128, 179, 255), (486, 318, 86, 76))
p.draw.ellipse(screen, 'Black', (486, 318, 86, 76), 1)
p.draw.circle(screen, 'Black', (527, 356), 12)

# HAIR
x = 255
y = 285
half_storon = 35*math.sqrt(3)
print(half_storon)
delta_posx = half_storon*math.cos(beta)
delta_angle = 15*grad
angle = math.atan(2)
delta_posy = half_storon*math.sin(beta)

for i in range(8):
    if i == 7:
        regular_polygon(screen, (212, 42, 255), 3, 180*grad, 485, y+8, 70)
    else:
        double_regular_polygon(screen, (212, 42, 255), 3, angle, x, y, 70)
    delta_posx = half_storon * math.cos(beta)
    delta_posy = half_storon * math.sin(beta)
    y -= delta_posy/2
    x += delta_posx/2
    angle += delta_angle
    delta_angle -= 3.5*grad

p.display.update()
clock = p.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in p.event.get():
        if event.type == p.QUIT:
            finished = True

p.quit()
