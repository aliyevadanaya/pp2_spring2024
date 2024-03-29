import pygame, os

pygame.init()
w, h = 500, 838
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('Music player')

images = {
    'run' : pygame.transform.scale(pygame.image.load(r'C:\Users\aliev\OneDrive\Рабочий стол\python\lab7\pictures\run.jpg'), (w, h)),
    'stop' : pygame.transform.scale(pygame.image.load(r'C:\Users\aliev\OneDrive\Рабочий стол\python\lab7\pictures\stop.jpg'), (w, h))
}

music_list = []
main_path = r"C:\Users\aliev\OneDrive\Рабочий стол\python\lab7"
class MUSIC:
    def __init__(self, name):
        self.path = main_path
        self.name = str(name)
        self.image = pygame.transform.scale(pygame.image.load(main_path+ f'\\pictures\\{self.name}.jpg'), (350, 350))
        self.music_path = main_path + f'\\music\\{self.name}.mp3'
        print(main_path+ f'\\pictures\\{self.name}.jpg')
        print(main_path + f'\\music\\{self.name}.mp3')
        print(self.image)
        


for i in os.listdir(main_path + '\\music'):
    print(i[:-4])
    music_list.append(MUSIC(i[:-4]))

# pygame.mixer.music.play(music_list[0].music)
        
run = False
clock = pygame.time.Clock()
active_order = 0

done = False
while not done:
    if run:
        screen.blit(images['run'], (0,0))
    else:
        screen.blit(images['stop'], (0,1))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if run:
                    pygame.mixer.music.pause()
                elif pygame.mixer.music.get_busy():
                    pygame.mixer.music.unpause()
                else:
                    pygame.mixer.music.load(music_list[active_order].music_path)
                    pygame.mixer.music.play()
                run = not run
            if event.key == pygame.K_RIGHT:
                active_order = (active_order+1)%len(music_list)
                if run:
                    pygame.mixer.music.stop()
                    run = not run
            if event.key == pygame.K_LEFT:
                active_order = (active_order-1)%len(music_list)
                if run:
                    pygame.mixer.music.stop()
                    run = not run
    
    screen.blit(music_list[active_order].image, music_list[active_order].image.get_rect(centerx = w//2, centery=h//3))
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()