import pygame, datetime
pygame.init()
screen = pygame.display.set_mode((1000, 750))
main_clock = pygame.image.load(r'C:\Users\aliev\OneDrive\Рабочий стол\python\lab7\pictures\mainclock.png')
main_clock = pygame.transform.scale(main_clock, (1000, 750))

right = pygame.transform.scale(pygame.image.load(r'C:\Users\aliev\OneDrive\Рабочий стол\python\lab7\pictures\rightarm.png'), (1000, 750))
right = pygame.transform.rotate(right, -55)
left = pygame.transform.scale(pygame.image.load(r'C:\Users\aliev\OneDrive\Рабочий стол\python\lab7\pictures\leftarm.png'), (45, 750))
left = pygame.transform.rotate(left, -3)
def draw_arm(arm, angle):
    arm = pygame.transform.rotate(arm, angle)
    rect_arm = arm.get_rect()
    rect_arm.centerx = 1000//2
    rect_arm.centery = 750//2
    screen.blit(arm, rect_arm)
def draw_time(m, s):
    font = pygame.font.SysFont(None, 30)
    m, s = int(m), int(s)
    text = f'{m}:{s//10}{s%10}'
    font = font.render(text, False, (0,0,255))
    screen.blit(font, (900, 700))
done = True
while done:
    m, s = datetime.datetime.now().minute, datetime.datetime.now().second
    screen.blit(main_clock, (0, 0))
    # screen.blit(left, (1000//2, 750//2))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
    draw_arm(left, -6*s)
    draw_arm(right, -6*m)
    draw_time(m,s)
    pygame.display.flip()