import pygame
from game_object import GameObject 
from worm import Worm
from food import Food
from wall import Wall
import random
import forsnakemain2


pygame.init()
screen = pygame.display.set_mode((900, 600))
def draw_score_level():
        fonts = pygame.font.SysFont("Verdana", 20)
        fontl = pygame.font.SysFont("Verdana", 20)
        texts = fonts.render(f"score: {Score}", True, (0, 0, 0))
        textl = fontl.render(f"level: {level}", True, (0, 0, 0))
        screen.blit(texts, (0, 0))
        screen.blit(textl, (0, 20))
def final():
        textfs = font.render(f"score: {Score}", True, (0, 0, 0))
        fontfl = pygame.font.SysFont("Verdana", 40)
        screen.blit(textfs, (900 // 2 - textfs.get_width() // 2, 320))
        textfl = font.render(f"level: {level}", True, (0, 0, 0))
        screen.blit(textfl, (900 // 2 - textfl.get_width() // 2, 270))

def create_background(screen, width, height):
        colors = [(255, 255, 255), (212, 212, 212)]
        tile_width = 20
        y = 0
        while y < height:
                x = 0
                while x < width:
                        row = y // tile_width
                        col = x // tile_width
                        pygame.draw.rect(screen, colors[(row + col) % 2],pygame.Rect(x, y, tile_width, tile_width))
                        x += tile_width
                y += tile_width

done = False
Score = 0
n_for_next_lvl = 10
level = 0
clock = pygame.time.Clock()
SPEED = 5+5
worm = Worm(20)
food = Food(20)
wall = Wall(20)


lose = False
pause = False

name = input("please write your name\n")
print(forsnakemain2.show(name))
forsnakemain2.add_user(name)

while not done:
        # Event filtering
        filtered_events = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    done = True
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        #print("you pressed")
                        if pause == False:    
                            pause = True
                        else:
                            pause = False
                        print(pause)
                        
            else:
                filtered_events.append(event)
        if (not lose and not pause):
                #print("condition1")
                worm.process_input(filtered_events)
                can_move = worm.can_going(wall.points)
                # print(can_move)
                if not can_move:
                        lose = True
                        continue
                worm.move()
                #print("worm can move")

                pos = food.can_eat(worm.points[0])
                if(pos != None):
                        Score += random.randint(1, 4)
                        worm.increase(pos)
                        food.random_food(wall.points + worm.points+food.points)
                food.points[0].time-=1
                if food.points[0].time<=0:
                        print("time over")
                        food.random_food(wall.points + worm.points+food.points)
                        
                
                if len(worm.points) > n_for_next_lvl:
                        print(1)
                        wall.next_level()
                        level += 1
                        n_for_next_lvl += 3
                        SPEED += 5
                create_background(screen, 900, 600)
                
                food.draw(screen)
                wall.draw(screen)
                worm.draw(screen)
                draw_score_level()
                forsnakemain2.addinfo(name, level, SPEED, Score)
        elif (not lose and pause):
                create_background(screen, 900, 600)
                food.draw(screen)
                worm.draw(screen)
                wall.draw(screen)
                #currentinfo = forsnake2.show(name)
                fontp = pygame.font.SysFont("Verdana", 40)
                textp = fontp.render(forsnakemain2.show(name), True, (51, 0, 102))
                screen.blit(textp, textp.get_rect(center = (900//2, 250)))
                
        else:
       
                font = pygame.font.SysFont("Verdana", 60)
                text = font.render("GAME OVER", True, (0, 0, 0))
                screen.fill((255, 0, 0))
                screen.blit(text, text.get_rect(center = (900//2, 250)))
                fontfs = pygame.font.SysFont("Verdana", 40)
                # textfs = font.render(f"score: {Score}", True, (0, 0, 0))
                # fontfl = pygame.font.SysFont("Verdana", 40)
                # screen.blit(textfs, (900 // 2 - textfs.get_width() // 2, 600 // 2 + 10))
                # textfl = font.render(f"level: {level}", True, (0, 0, 0))
                # screen.blit(textfl, (900 // 2 - textfl.get_width() // 2, 600 // 2 + 60))
                final()
                
                
                
        
        pygame.display.flip()
        clock.tick(SPEED)