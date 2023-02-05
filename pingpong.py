import pygame as p
from paddles import Paddle

p.init()


BLACK = (0,0,0)
WHITE = (255,255,255)

win_width = 700
win_height = 500
window = p.display.set_mode((win_width, win_height))
p.display.set_caption("Pong")

paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200

paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200

p.all_sprites_list = p.sprite.Group()

p.all_sprites_list.add(paddleA)
p.all_sprites_list.add(paddleB)

play = True

clock = p.time.Clock()

while play:
    for event in p.event.get():
        if event.type == p.QUIT:
            play = False

p.Surface.fill(BLACK)
p.draw.line(p.display, WHITE, [349, 0], [349, 500], 5)

clock.tick(60)

p.display.update()