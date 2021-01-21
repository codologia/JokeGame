import pygame as pg

FPS = 30

pg.init()
screen = pg.display.set_mode((640, 480))
clock = pg.time.Clock()

# Класс, который описывает любую кнопку
class Button:
    UP = 0 # Кнопка не нажата
    DOWN = 1 # Кнопка нажата
    def __init__(self, color, pos, width = 80, height = 30):
        self.color = color
        self.pos = pos
        self.width = width
        self.height = height
        state = Button.UP # Состояние кнопки
    
    def draw(self):
        pg.draw.rect(screen, self.color, (self.pos.x, self.pos.y,
                                          self.width, self.height))

    def is_in(self, point):
        A = self.pos
        C = Point(self.pos.x + self.width, self.pos.y + self.height)
        return A.x <= point.x <= C.x and A.y <= point.y <= C.y

running = True
while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

pg.quit()