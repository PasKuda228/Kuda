from pygame import *
from random import *
from time import time as timer

class GameSprite(sprite.Sprite):
    def __init__(self, p_image, p_x, p_y, sx, sy, p_speed):
        super().__init__()
        self.sx = sx
        self.sy = sy
        self.image = transform.scale(image.load(p_image),(sx, sy))
        self.speed = p_speed
        self.rect = self.image.get_rect()
        self.rect.x = p_x
        self.rect.y = p_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 440:
            self.rect.y += self.speed
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 440:
            self.rect.y += self.speed

window = display.set_mode((700, 500), RESIZABLE)
display.set_caption('Ping-pong')


shooter = transform.scale(image.load('fon.jpg'),(700, 500))

tennis = GameSprite('tennis.png', 200, 200 , 50, 50, 4) 
platforma1 = Player('patforma.png', 10, 200, 30, 120, 4)
platforma2 = Player('patforma.png', 640, 200, 30, 120, 4)

mixer.init()
mixer.music.load('m.ogg')
mixer.music.play()
fire_s = mixer.Sound('fire.ogg')

font.init()
font1 = font.SysFont('Arial', 70)
win1 = font1.render('Победа 1', True, (0, 215, 0))
win2 = font1.render('Победа 2', True, (0, 215, 0))

vx = 5
vy = 5

game = True
finish = False
clock = time.Clock()
while game:
  
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish == False:
        window.blit(shooter, (0, 0))
        tennis.reset()
        platforma1.reset()
        platforma2.reset()

        platforma1.update_l()
        platforma2.update_r()
        tennis.rect.x += vx    
        tennis.rect.y += vy

        if sprite.collide_rect(platforma1, tennis) or sprite.collide_rect(platforma2, tennis):
            fire_s.play()
            vx *= -1
        if tennis.rect.y < 0 or tennis.rect.y > 450:
            vy *= -1
        if tennis.rect.x < 0:
            finish = True
            window.blit(win2, (200, 200))
            game = True
        if tennis.rect.x > 650:
            finish = True
            window.blit(win1, (200, 200))
            game = True

    display.update()
    clock.tick(60)
