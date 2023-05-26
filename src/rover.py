import pygame
import math


class Rover(pygame.sprite.Sprite):
    id = 0

    def __init__(self, surface, coord=(0,0), speed=10):
        Rover.id += 1
        self.x, self.y = coord
        self.surface = surface
        self.w = pygame.display.get_surface().get_width()
        self.h = pygame.display.get_surface().get_height()
        self.angle = 0
        self.x_rover = 0
        self.y_rover = 0
        self.speed = speed

    def set_xy(self, coord):
        self.x, self.y = coord

    def get_xy(self):
        return self.x, self.y

    @staticmethod
    def get_id():
        return Rover.id

    def right(self, angle):
        self.angle -= 1/8

    def left(self, angle):
        self.angle += angle

    def go(self, direction="FORWARD", length=100):
        self.x_rover = length * math.cos(self.angle)
        self.y_rover = length * math.sin(self.angle)

    def draw(self, coord):
        x, y = coord
        coord_rover = x+self.w//2 + self.x_rover, y+self.h//2 + self.y_rover
        rover_rect = pygame.draw.circle(self.surface, "GREY", coord_rover, 15)






