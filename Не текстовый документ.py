from pygame import *
from pygame import time
from random import randint
from time import time as timer


class Gamesprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y , player_speed,width = 50,heght=50):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(width,heght))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y)) 







class Player(Gamesprite):
    def update(self):
        if keys_pressed[K_d]:
            self.direction="right"
            self.rect.x +=5
            
        if keys_pressed[K_a]:
            self.direction="left"
            self.rect.x -=5






