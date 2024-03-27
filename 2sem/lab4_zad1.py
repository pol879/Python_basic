import pygame as p


p.init()
# def
FPS = 30
screen = p.display.set_mode((400, 400))
surface = p.Surface((400, 400))
surface.fill((217,217,217))

# display
screen.blit(surface, (0, 0))
p.draw.circle(screen, (255,255,0), (200, 200), 100)
p.draw.circle(screen, (0,0,0), (200, 200), 100, 2)
# mouth
p.draw.line(screen, (0,0,0), (150,250), (250, 250), 20)
# left eye
p.draw.circle(screen, (250,0,0), (150,180), 20)
p.draw.circle(screen, (0,0,0), (150,180), 8)
p.draw.circle(screen, (0,0,0), (150,180), 20, 2)
# right eye
p.draw.circle(screen, (250,0,0), (250,180), 16)
p.draw.circle(screen, (0,0,0), (250,180), 8)
p.draw.circle(screen, (0,0,0), (250,180), 16, 2)
# eyebrows
p.draw.polygon(screen, (0,0,0), [(102, 117), (182, 167), (177, 175), (98, 125)])
p.draw.polygon(screen, (0,0,0), [(218, 166), (298, 136), (302, 145), (222, 175)])
p.display.update()
clock = p.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in p.event.get():
        if event.type == p.QUIT:
            finished = True

p.quit()
