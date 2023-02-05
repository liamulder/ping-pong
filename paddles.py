from pygame import sprite, Surface, draw

BLACK = (0,0,0)

class Paddle(sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        self.image = Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        draw.rect(self.image, color, [0, 0, width, height])

        self.rect = self.image.get_rect()
