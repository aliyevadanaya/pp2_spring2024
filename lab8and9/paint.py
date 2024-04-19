import pygame
pygame.init()
screen = pygame.display.set_mode((1200, 800))
main_surf = pygame.Surface(screen.get_size())
# drawing_surf = pygame.Surface(screen.get_size())
CURRENT_COLOR = (255,255,255)
rect_stata = [0, 0, 0, 0]
circle_stata = [0, 0, 0]
square_stata = [0, 0, 0]
eraser_stata = [0, 0, 0, 0]
etriangle_stata = [0, 0, 0, 0]
rtriangle_stata = [0, 0, 0, 0]
rhombus_stata = [0, 0, 0, 0]

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
    elif TOOL == 'square':
        pygame.draw.rect(screen, CURRENT_COLOR, (square_stata[0], square_stata[1], square_stata[2], square_stata[2]), 2)
    elif TOOL == 'e-triangle':
        pygame.draw.aalines(screen, CURRENT_COLOR, True, [(etriangle_stata[0], etriangle_stata[1]+etriangle_stata[3]), (etriangle_stata[0]+etriangle_stata[2], etriangle_stata[1]+etriangle_stata[3]), (etriangle_stata[0]+(etriangle_stata[2])//2, etriangle_stata[1])], 1 )
        # pygame.draw.polygon(screen, CURRENT_COLOR, [(etriangle_stata[0], etriangle_stata[1]+etriangle_stata[3]), (etriangle_stata[0]+etriangle_stata[2], etriangle_stata[1]+etriangle_stata[3]), (etriangle_stata[0]+(etriangle_stata[2])//2, etriangle_stata[1])], 1)
    elif TOOL == "r-triangle":
        pygame.draw.aalines(screen, CURRENT_COLOR, True, [(rtriangle_stata[0], rtriangle_stata[1]), (rtriangle_stata[0]+rtriangle_stata[2], rtriangle_stata[1]+rtriangle_stata[3]), (rtriangle_stata[0], rtriangle_stata[1]+rtriangle_stata[3])], 2)
    elif TOOL == 'rhombus':
        pygame.draw.polygon(screen, CURRENT_COLOR, [(rhombus_stata[0] + rhombus_stata[2]//2, rhombus_stata[1]), (rhombus_stata[0] + rhombus_stata[2], rhombus_stata[1] + rhombus_stata[3]//2), (rhombus_stata[0] + rhombus_stata[2]//2, rhombus_stata[1] + rhombus_stata[3]), (rhombus_stata[0], rhombus_stata[1] + rhombus_stata[3]//2)], 2)
           
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
            elif event.key == pygame.K_p and TOOL == 'choose color':
                CURRENT_COLOR = (128, 0, 128)
            elif event.key == pygame.K_l and TOOL == 'choose color':
                CURRENT_COLOR = (0, 255, 0)
                
            elif event.key == pygame.K_5 or event.key == pygame.K_KP_5:
                TOOL = 'square'
            elif event.key == pygame.K_6 or event.key == pygame.K_KP_6:
                TOOL = 'e-triangle'
            elif event.key == pygame.K_7 or event.key == pygame.K_KP_7:
                TOOL = 'r-triangle'
            elif event.key == pygame.K_8 or event.key == pygame.K_KP_8:
                TOOL = 'rhombus'
            
        

        
                
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
                elif TOOL == 'square':
                    pygame.draw.rect(main_surf, CURRENT_COLOR, (square_stata[0], square_stata[1], square_stata[2], square_stata[2]), 2)
                elif TOOL == 'e-triangle':
                    pygame.draw.aalines(main_surf, CURRENT_COLOR, True, [(etriangle_stata[0], etriangle_stata[1]+etriangle_stata[3]), (etriangle_stata[0]+etriangle_stata[2], etriangle_stata[1]+etriangle_stata[3]), (etriangle_stata[0]+(etriangle_stata[2])//2, etriangle_stata[1])], 1 )
                    # pygame.draw.polygon(main_surf, CURRENT_COLOR, [(etriangle_stata[0], etriangle_stata[1]+etriangle_stata[3]), (etriangle_stata[0]+etriangle_stata[2], etriangle_stata[1]+etriangle_stata[3]), (etriangle_stata[0]+(etriangle_stata[2])//2, etriangle_stata[1])], 1)
                elif TOOL == 'r-triangle':
                    pygame.draw.aalines(main_surf, CURRENT_COLOR, True, [(rtriangle_stata[0], rtriangle_stata[1]), (rtriangle_stata[0]+rtriangle_stata[2], rtriangle_stata[1]+rtriangle_stata[3]), (rtriangle_stata[0], rtriangle_stata[1]+rtriangle_stata[3])], 2)
               # elif TOOL == 'rhombus':
                elif TOOL == 'rhombus':
                   pygame.draw.polygon(main_surf, CURRENT_COLOR, [(rhombus_stata[0] + rhombus_stata[2]//2, rhombus_stata[1]), (rhombus_stata[0] + rhombus_stata[2], rhombus_stata[1] + rhombus_stata[3]//2), (rhombus_stata[0] + rhombus_stata[2]//2, rhombus_stata[1] + rhombus_stata[3]), (rhombus_stata[0], rhombus_stata[1] + rhombus_stata[3]//2)], 2)
           
                    
                    
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
                if TOOL == 'square':
                    end_pos = event.pos
                    w = abs(end_pos[0] - start_pos[0])
                    h = abs(end_pos[1] - start_pos[1])
                    w = min(w, h)
                    h = w
                    square_stata[2] = w
                    if end_pos[0] >= start_pos[0] and end_pos[1] >= start_pos[1]:
                        square_stata[0] = start_pos[0]
                        square_stata[1] = start_pos[1]
                    elif end_pos[0] <= start_pos[0] and end_pos[1] >= start_pos[1]:
                        square_stata[0] = start_pos[0] - w
                        square_stata[1] = start_pos[1]
                    elif end_pos[0] >= start_pos[0] and end_pos[1] <= start_pos[1]:
                        square_stata[0] = start_pos[0]
                        square_stata[1] = start_pos[1] - w
                    else:
                        square_stata[0] = start_pos[0] - w
                        square_stata[1] = start_pos[1] - w
                    pygame.draw.rect(screen, CURRENT_COLOR, (square_stata[0], square_stata[1], square_stata[2], square_stata[2]), 2)
                if TOOL == 'eraser':
                    end_pos = event.pos
                    pygame.draw.line(main_surf, (0, 0, 0), eraser_stata, end_pos, 20)
                    eraser_stata = list(end_pos)
                if TOOL == 'e-triangle':
                    end_pos = event.pos
                    w = abs(end_pos[0] - start_pos[0])
                    h = abs(end_pos[1] - start_pos[1])
                    h = min(h, (w*3**0.5)//2)
                    w = h*2/(3**0.5)
                    etriangle_stata[2] = w
                    etriangle_stata[3] = h
                    if end_pos[0] >= start_pos[0] and end_pos[1] >= start_pos[1]:
                        etriangle_stata[0] = start_pos[0]
                        etriangle_stata[1] = start_pos[1]
                    elif end_pos[0] <= start_pos[0] and end_pos[1] >= start_pos[1]:
                        etriangle_stata[0] = start_pos[0] - w
                        etriangle_stata[1] = start_pos[1]
                    elif end_pos[0] >= start_pos[0] and end_pos[1] <= start_pos[1]:
                        etriangle_stata[0] = start_pos[0]
                        etriangle_stata[1] = start_pos[1] - w
                    else:
                        etriangle_stata[0] = start_pos[0] - w
                        etriangle_stata[1] = start_pos[1] - w
                    pygame.draw.aalines(screen, CURRENT_COLOR, True, [(etriangle_stata[0], etriangle_stata[1]+etriangle_stata[3]), (etriangle_stata[0]+etriangle_stata[2], etriangle_stata[1]+etriangle_stata[3]), (etriangle_stata[0]+(etriangle_stata[2])//2, etriangle_stata[1])], 1 )
                    # pygame.draw.polygon(screen, CURRENT_COLOR, [(etriangle_stata[0], etriangle_stata[1]+etriangle_stata[3]), (etriangle_stata[0]+etriangle_stata[2], etriangle_stata[1]+etriangle_stata[3]), (etriangle_stata[0]+(etriangle_stata[2])//2, etriangle_stata[1])], 1)
                if TOOL == 'r-triangle':
                    end_pos = event.pos
                    rtriangle_stata[0] = min(start_pos[0], end_pos[0])
                    rtriangle_stata[1] =  min(start_pos[1], end_pos[1])
                    rtriangle_stata[2] = abs(end_pos[0] - start_pos[0])
                    rtriangle_stata[3] = abs(end_pos[1] - start_pos[1])
                    pygame.draw.aalines(screen, CURRENT_COLOR, True, [(rtriangle_stata[0], rtriangle_stata[1]), (rtriangle_stata[0]+rtriangle_stata[2], rtriangle_stata[1]+rtriangle_stata[3]), (rtriangle_stata[0], rtriangle_stata[1]+rtriangle_stata[3])], 2)
                if TOOL == 'rhombus':
                    end_pos = event.pos
                    w = abs(end_pos[0] - start_pos[0])
                    h = abs(end_pos[1] - start_pos[1])
                    if end_pos[0] >= start_pos[0] and end_pos[1] >= start_pos[1]:
                        rhombus_stata[0] = start_pos[0] - w//2
                        rhombus_stata[1] = start_pos[1] - h//2
                    elif end_pos[0] <= start_pos[0] and end_pos[1] >= start_pos[1]:
                        rhombus_stata[0] = start_pos[0] + w//2
                        rhombus_stata[1] = start_pos[1] - h//2
                    elif end_pos[0] >= start_pos[0] and end_pos[1] <= start_pos[1]:
                        rhombus_stata[0] = start_pos[0] - w//2
                        rhombus_stata[1] = start_pos[1] + h//2
                    else:
                        rhombus_stata[0] = start_pos[0] + w//2
                        rhombus_stata[1] = start_pos[1] + h//2
                    rhombus_stata[2] = w
                    rhombus_stata[3] = h
                    pygame.draw.polygon(screen, CURRENT_COLOR, [(rhombus_stata[0] + rhombus_stata[2]//2, rhombus_stata[1]), (rhombus_stata[0] + rhombus_stata[2], rhombus_stata[1] + rhombus_stata[3]//2), (rhombus_stata[0] + rhombus_stata[2]//2, rhombus_stata[1] + rhombus_stata[3]), (rhombus_stata[0], rhombus_stata[1] + rhombus_stata[3]//2)], 2)
           
    draw_mode()
    draw_color()
    pygame.display.flip() 
    
    

pygame.quit()
