from pygame import *
from pygame.locals import *
from utilities.constants import *
import numpy as np

def draw_everything(disp):
    global character_rect, game_terrain_rect_list
    disp.fill(screen_color)
    
    #? Draw character
    character_rect = draw.rect(disp, character_color, (character_position[0], character_position[1], character_dimentions[0], character_dimentions[1]))
    
    #? Draw ground
    draw.rect(disp, ground_color, (0, screen_height-ground_height, screen_width, ground_height))

    #? Draw terrain
    game_terrain_rect_list = []
    for index, terrain in enumerate(game_terrain):
        game_terrain[index][0] -= game_speed
        if game_terrain[index][0] < -game_terrain_dimentions[0]:
            game_terrain.remove(game_terrain[index])
        game_terrain_rect_list.append(draw.rect(disp, game_terrain_color, (terrain[0], terrain[1], game_terrain_dimentions[0], game_terrain_dimentions[1])))

    display.update()

def generate_terrain():
    if np.random.randint(0, game_terrain_generate_probability) == 0:
        game_terrain.append([screen_width, screen_height-ground_height-game_terrain_dimentions[1]])
    for index, terrain in enumerate(game_terrain[:-1]):
        if abs(terrain[0] - game_terrain[index+1][0]) < game_terrain_minimum_distance_to_each_other+game_terrain_dimentions[0]:
            game_terrain.remove(game_terrain[index+1])

def command_jump():
    global character_on_ground, character_velocity
    if character_on_ground:
        character_on_ground = False
        character_velocity = character_jump_power

def character_jump():
    global character_on_ground, character_velocity
    if character_on_ground == False:
        character_position[1] -= character_velocity
        character_velocity -= character_gravity
        if character_position[1] >= screen_height-ground_height-character_dimentions[1]:
            character_on_ground = True
            character_position[1] = character_initial_position[1]
            character_velocity = 0

def collision_checker(disp):
    global character_rect, game_terrain_rect_list
    for terrain_rect in game_terrain_rect_list:
        if character_rect.colliderect(terrain_rect):
            return True
    return False
