import pygame
from time import sleep

# dataset constants
#name = 'dogs'
#tests_number = 10
#r_values = [5, 8, 10, 12, 15, 17, 20]
#c_values = [30, 15, 10, 5]
#image_width, image_height = 120, 90
#mods = ['rgb', 'hsv']

name = 'people'
tests_number = 40
r_values = [2, 3, 4, 5, 8, 10, 16]
c_values = [16, 8, 4, 2]
image_width, image_height = 120, 90
mods = ['rgb', 'hsv']




# visualisation constants
scale = 2
border_size = 10

DISPLAY = (image_width*scale*7+border_size*6, image_height*scale*4+border_size*3)
pygame.init()
flags = pygame.DOUBLEBUF | pygame.HWSURFACE
screen = pygame.display.set_mode(DISPLAY, flags)
background = pygame.Surface(DISPLAY)
background.fill(pygame.Color("#000000"))
for test in range(1, tests_number):
    for mode in mods:
        pygame.display.set_caption(mode+str(test))
        for ri in range(7):
            for ci in range(4):
                path = 'results/'+name+'/'+mode+'-'+str(r_values[ri])+'-'+str(c_values[ci])+'/test'+str(test)+mode+'.png'
                img = pygame.image.load(path)
                img = pygame.transform.scale(img, [image_width*scale, image_height*scale])
                screen.blit(img, [(image_width*scale+border_size)*ri, (image_height*scale+border_size)*ci])
        pygame.display.update()
        save_as = 'results/'+name+'/comparison-test'+str(test)+'-'+mode+'.png'
        pygame.image.save(screen, save_as)
        sleep(1)