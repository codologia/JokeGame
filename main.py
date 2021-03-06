import pygame as pg
import Colors as color
import random as rnd

FPS = 30

class Window:
    WIDTH = 350
    HEIGHT = 200

pg.init()
screen = pg.display.set_mode((Window.WIDTH, Window.HEIGHT))
clock = pg.time.Clock()

font = pg.font.SysFont('arial', 30)
text_question = font.render('Ты доволен зарплатой?', True, color.BLACK)
text_yes = font.render('YES', True, color.BLACK)
text_no = font.render('NO', True, color.BLACK)

# Структура, которая хранит номера кнопок
class MouseButton:
    LEFT   = 1
    MIDDLE = 2
    RIGHT  = 3

# Класс, который описывает любую точку
class Point:
    x = 0; y = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Класс, который описывает любую кнопку
class Button:
    UP = 0 # Кнопка не нажата
    DOWN = 1 # Кнопка нажата
    def __init__(self, pg_text, color, position, width = 80, height = 30):
        self.pg_text = pg_text
        self.color = color
        self.position = position
        self.width = width
        self.height = height
        self.state = Button.UP # Состояние кнопки
        self.is_over = False
        self.is_click = False
    
    def draw(self):
        pg.draw.rect(screen, self.color, (self.position.x, self.position.y,
                                          self.width, self.height))
        screen.blit(self.pg_text, (self.position.x, self.position.y))
        
    def jumpto(self, position):
        self.position = position
        self.change_color()

    def is_in(self, point):
        A = self.position
        C = Point(self.position.x + self.width, self.position.y + self.height)
        return A.x <= point.x <= C.x and A.y <= point.y <= C.y
    
    def delete(self):
        self.position = Point(-1, -1)
        self.width = 0
        self.height = 0
    
    def change_color(self):
        R = rnd.randint(0, 255)
        G = rnd.randint(0, 255)
        B = rnd.randint(0, 255)
        self.color = (R, G, B)

btn_yes = Button(text_yes, color.RED, Point(70, 100)) # Создание кнопки YES
btn_no = Button(text_no, color.RED, Point(170, 100)) # Создание кнопки NO

btn_yes_counter = 0

running = True
while running:
    screen.fill(color.WHITE) # Заливка экрана черным цветом
    clock.tick(FPS)
    
    listEvents = pg.event.get() # Список событий пользовател в программе
    for event in listEvents:
        if event.type == pg.QUIT:
            running = False
        # Взаимодействие с пользователем
        # MOUSEMOTION - событие перемещения мышки
        if event.type == pg.MOUSEMOTION:
            mouse_pos = Point(event.pos[0], event.pos[1]) # Позиция мышки
            # Если мышка попала на кнопку NO
            if btn_no.is_in(mouse_pos):
                # Задать кнопке новую позицию
                btn_no.jumpto(Point(rnd.randint(0, Window.WIDTH), rnd.randint(0, Window.HEIGHT)))
            # Попала ли мышка на кнопку YES
            if btn_yes.is_in(mouse_pos):
                btn_yes.is_over = True # Мышка над кнопкой
            else:
                btn_yes.is_over = False # Мышка ушла с кнопки
        # MOUSEBUTTONDOWN - событие нажатие левой кнопки мышки
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == MouseButton.LEFT and btn_yes.is_over == True: # Нажата ЛКМ
                btn_yes.is_click = True
    
    # Обработка нажатий
    if btn_yes.is_click == True:
        btn_yes.is_click = False # Клик завершен
        btn_yes_counter += 1 # Увеличиваем счетчик нажатий
        # Обработка каждого ответа
        if btn_yes_counter == 1: # Первый ответ
            text_question = font.render('Ты уверен?', True, color.BLACK)
            btn_yes.color = color.GREEN
        if btn_yes_counter == 2: 
            text_question = font.render('Ты точно уверен?', True, color.BLACK)
            btn_yes.color = color.BLUE
        if btn_yes_counter == 3:
            text_question = font.render('Я очень рад', True, color.RED)
            
    screen.blit(text_question, (50, 10))
    if btn_yes_counter < 3:
        btn_yes.draw() # Рисование кнопки YES
        btn_no.draw()  # Рисование кнопки NO
    else:
        btn_yes.delete() # Рисование кнопки YES
        btn_no.delete()  # Рисование кнопки NO
    
    pg.display.update() # Перерисока экрана

pg.quit()