from engine.datasets import *

#test_people_64x48(41, 5, 4, 8, 'rgb')

#for radius in [5, 8, 10, 12, 15, 17, 20]:
#    for cell_size in [30, 15, 10, 5]:
#        test_dogs_120x90(9, 3, radius, cell_size, 'rgb', subfolder='/rgb'+'-'+str(radius)+'-'+str(cell_size)+'/')
#        test_dogs_120x90(9, 3, radius, cell_size, 'hsv', subfolder='/hsv'+'-'+str(radius)+'-'+str(cell_size)+'/')

for radius in [2, 3, 4, 5, 8, 10, 16]:
    for cell_size in [16, 8, 4, 2]:
        test_people_64x48(40, 3, radius, cell_size, 'rgb', subfolder='/rgb'+'-'+str(radius)+'-'+str(cell_size)+'/')
        test_people_64x48(40, 3, radius, cell_size, 'hsv', subfolder='/hsv'+'-'+str(radius)+'-'+str(cell_size)+'/')