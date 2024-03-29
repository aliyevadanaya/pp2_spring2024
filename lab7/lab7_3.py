import pygame

pygame.init()

screen = pygame.display.set_mode((400,500))
x, y = 400//2, 500//2
clock = pygame.time.Clock()
run = True

while run:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        y = max(y-20, 25)
    if keys[pygame.K_DOWN]:
        y=min(y+20, 475)
    if keys[pygame.K_LEFT]:
        x=max(x-20, 25)
    if keys[pygame.K_RIGHT]:
        x=min(x+20, 375)
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 25)
    pygame.display.update()
    clock.tick(60)