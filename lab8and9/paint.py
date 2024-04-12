import pygame
pygame.init()
screen = pygame.display.set_mode((1000, 750))
main_surf = pygame.Surface(screen.get_size())
# drawing_surf = pygame.Surface(screen.get_size())
CURRENT_COLOR = (255,255,255)
rect_stata = [0, 0, 0, 0]
circle_stata = [0, 0, 0]
eraser_stata = [0, 0]

TOOL = None
run = True
drawing = False  
start_pos = None 

def draw_mode():
    font = pygame.font.SysFont(None, 30)
    text = f"mode: {TOOL}"
    text = font.render(text, True, (255,255,255))
    screen.blit(text, (10, 10))

def draw_color():
    font = pygame.font.SysFont(None, 30)
    text = f"color"    
    text = font.render(text, True, CURRENT_COLOR)
    screen.blit(text, (10, 40))

while run:
    screen.blit(main_surf, (0, 0))
    if TOOL == 'rect' and rect_stata[2] != 0:
        pygame.draw.rect(screen, CURRENT_COLOR, pygame.Rect(rect_stata[0], rect_stata[1], rect_stata[2], rect_stata[3]), 2) 
        
    elif TOOL == 'circle' and rect_stata[2] != 0:
        pygame.draw.circle(screen, CURRENT_COLOR, (circle_stata[0]+circle_stata[2], circle_stata[1]+circle_stata[2]), circle_stata[2], 2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1 or event.key == pygame.K_KP_1:
                TOOL = 'rect'
            elif event.key == pygame.K_2 or event.key == pygame.K_KP_2:
                TOOL = 'circle'
            elif event.key == pygame.K_3 or event.key == pygame.K_KP_3:
                TOOL = 'eraser'
                
            elif event.key == pygame.K_4 or event.key == pygame.K_KP_4:
                TOOL = 'choose color'
            elif event.key == pygame.K_r and TOOL == 'choose color':
                CURRENT_COLOR = (255, 0, 0)
            elif event.key == pygame.K_b and TOOL == 'choose color':
                CURRENT_COLOR = (0, 191, 255)
            elif event.key == pygame.K_y and TOOL == 'choose color':
                CURRENT_COLOR = (255, 255, 0)
            elif event.key == pygame.K_g and TOOL == 'choose color':
                CURRENT_COLOR = (0, 128, 0)
                
           
        

        
                
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  
                start_pos = event.pos
                if TOOL== 'eraser':
                    eraser_stata = list(start_pos)
                copy_st_pos = list(start_pos)
                drawing = True 
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1: 
                drawing = False  
                if TOOL == 'rect':
                    pygame.draw.rect(main_surf, CURRENT_COLOR, pygame.Rect(rect_stata[0], rect_stata[1], rect_stata[2], rect_stata[3]), 2) 
                elif TOOL == 'circle':
                    pygame.draw.circle(main_surf, CURRENT_COLOR, (circle_stata[0]+circle_stata[2], circle_stata[1]+circle_stata[2]), circle_stata[2], 2)
        elif event.type == pygame.MOUSEMOTION:
            if drawing:
                if TOOL == 'rect':  
                    end_pos = event.pos
                    rect_stata[0] = min(start_pos[0], end_pos[0])
                    rect_stata[1] =  min(start_pos[1], end_pos[1])
                    rect_stata[2] = abs(end_pos[0] - start_pos[0])
                    rect_stata[3] = abs(end_pos[1] - start_pos[1])
                    pygame.draw.rect(screen, CURRENT_COLOR,  pygame.Rect(rect_stata[0], rect_stata[1], rect_stata[2], rect_stata[3]), 2) 
                if TOOL == 'circle':
                    end_pos = event.pos
                    w = abs(end_pos[0] - start_pos[0])
                    h = abs(end_pos[1] - start_pos[1])
                    w = min(w, h)
                    h = w
                    circle_stata[2] = w/2
                    if end_pos[0] >= start_pos[0] and end_pos[1] >= start_pos[1]:
                        circle_stata[0] = start_pos[0]
                        circle_stata[1] = start_pos[1]
                    elif end_pos[0] <= start_pos[0] and end_pos[1] >= start_pos[1]:
                        circle_stata[0] = start_pos[0] - w
                        circle_stata[1] = start_pos[1]
                    elif end_pos[0] >= start_pos[0] and end_pos[1] <= start_pos[1]:
                        circle_stata[0] = start_pos[0]
                        circle_stata[1] = start_pos[1] - w
                    else:
                        circle_stata[0] = start_pos[0] - w
                        circle_stata[1] = start_pos[1] - w
                    pygame.draw.circle(screen, CURRENT_COLOR, (circle_stata[0]+circle_stata[2], circle_stata[1]+circle_stata[2]), circle_stata[2], 2)
                
                if TOOL == 'eraser':
                    end_pos = event.pos
                    pygame.draw.line(main_surf, (0, 0, 0), eraser_stata, end_pos, 20)
                    eraser_stata = list(end_pos)
    draw_mode()
    draw_color()
    pygame.display.flip() 
    
    

pygame.quit()
