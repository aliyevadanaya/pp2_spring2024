import pygame
from game_object import GameObject 
from game_object import Point 
import random
class Food(GameObject):
    def __init__(self, tile_width):
        super().__init__([Point(120, 20)],(0,255,0), tile_width)
        
        
        
    
    def can_eat(self, head_location): # worm.points[0]
        result = None
        for point in self.points:
            if point.X == head_location.X and point.Y == head_location.Y:
                result = point
                break
        return result
    def random_food(self, occupied_points = None): # occupied points = worm.points + wall.points
        all_points = []
        occupied = [(point.X, point.Y) for point in occupied_points]
        for x in range(45): #30
            for y in range(30): #45
                if (x, y) not in occupied:
                    all_points.append((x*20, y*20))
        # self.rect = self.image.get_rect()
        points = random.choice(all_points)
        self.points[0] = Point(points[0], points[1])
        