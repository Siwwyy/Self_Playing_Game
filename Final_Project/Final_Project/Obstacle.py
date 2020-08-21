import pygame, sys
from pygame.math import Vector2

class Obstacle(object):

    def __init__(self,game,pos_x, pos_y):
        self.game = game
        self.basic_position = Vector2(pos_x,pos_y)
        self.position = Vector2(pos_x,pos_y)    #basic draw coordinates

    def move_by_coordinates(self,x,y):
        self.position.y += y

    def draw(self):
        rectangle = pygame.Rect(self.position.x,self.position.y,100,100)
        pygame.draw.rect(self.game.screen, (200,0,0), rectangle)

    def Get_Position(self):
        return Vector2(self.position)

    def Get_Basic_Position(self):
        return Vector2(self.basic_position)