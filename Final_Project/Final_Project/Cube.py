import pygame, sys
from pygame.math import Vector2

class Cube(object):

    def __init__(self,game,pos_x, pos_y):
        self.game = game
        self.position = Vector2(pos_x,pos_y)    #basic draw coordinates
        self.velocity = Vector2(0,0)

    def move(self, event_type):
        #Inputif 
        if event_type.type == pygame.KEYDOWN and event_type.key == pygame.K_RIGHT:
            if self.position.x + 100 < self.game.screen.get_size()[0]:
                self.position.x += 100
        if event_type.type == pygame.KEYDOWN and event_type.key == pygame.K_LEFT:
            if self.position.x - 100 >= 0:
                self.position.x += -100

    def move_by_coordinates(self,x):
        if self.position.x + 100 < self.game.screen.get_size()[0] and self.position.x >= 0:
            self.position.x += x

    def draw(self):
        rectangle = pygame.Rect(self.position.x,self.position.y,100,100)
        pygame.draw.rect(self.game.screen, (0,150,255), rectangle)

    def Get_Position(self):
        return Vector2(self.position)