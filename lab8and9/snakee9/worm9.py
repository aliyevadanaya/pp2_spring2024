import pygame
from game_object import GameObject 
from game_object import Point 

class Worm(GameObject):
    def __init__(self, tile_width):
        super().__init__([Point(20, 20)],(0,0,255), tile_width)
        self.DX = 0
        self.DY = 0

    def move(self):
        
        for i in range(len(self.points) - 1, 0, -1):
            self.points[i].X = self.points[i - 1].X
            self.points[i].Y = self.points[i - 1].Y

        self.points[0].X += self.DX * self.tile_width
        self.points[0].Y += self.DY * self.tile_width
        
    def can_going(self, wall_points):
        new_headx = self.points[0].X +  self.DX * self.tile_width
        new_heady = self.points[0].Y +  self.DY * self.tile_width
        if new_headx >= 900:
            return False
        elif new_headx < 0:
            return False
        if new_heady >= 600:
            return False
        elif new_heady < 0:
            return False
        for point in wall_points:
            if new_headx == point.X and new_heady == point.Y: 
                return False
        body = list(self.points)
        body.pop(0)
        for point in body:
            if new_headx == point.X and new_heady == point.Y: 
                return False
        return True
        
    def draw(self, screen):
        GameObject.draw(self, screen)
        pygame.draw.rect(screen, [219, 112, 147], pygame.Rect(self.points[0].X, self.points[0].Y, self.tile_width, self.tile_width))
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(self.points[0].X, self.points[0].Y, self.tile_width, self.tile_width), 1)
            
    def increase(self, pos):
        self.points.append(Point(pos.X, pos.Y))

    def process_input(self,  events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                self.DX = 0
                self.DY = -1
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                self.DX = 0
                self.DY = 1
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                self.DX = 1
                self.DY = 0
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                self.DX = -1
                self.DY = 0