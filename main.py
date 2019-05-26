from pygame import *
from pygame.locals import *
import numpy
from utilities.constants import *
from utilities.functions import *
from time import sleep

disp = display.set_mode((screen_width, screen_height), 0, 32)

#? Is game over yet?
end = False

while not end:
    #? Draw everything
    draw_everything(disp)

    #? Close game
    for e in event.get():
        if e.type==QUIT:
            quit()
            sys.exit()
    
    #? Get keyvoard input
    keys = key.get_pressed()
    if keys[K_UP]:
        command_jump()

    #? Generate terrain
    generate_terrain()

    #? Character
    character_jump()

    #? Collision checker
    end = collision_checker(disp)

    sleep(screen_sleep)

