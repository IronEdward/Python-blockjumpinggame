"""CONSTANTS"""

#* Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

#* Screen dimensions
screen_width = 1000
screen_height = 600
screen_color = WHITE
screen_sleep = 0.01

#* Ground
ground_height = 40
ground_color = BLACK

#* Screen(Gameplay)
game_speed = 10
game_terrain = []
game_terrain_dimentions = (30, 100)
game_terrain_color = GREEN
game_terrain_generate_probability = 50
game_terrain_minimum_distance_to_each_other = 500
game_terrain_rect_list = []

#* Character
character_dimentions = (50, 50)
character_initial_position = (100, screen_height - character_dimentions[1] - ground_height)
character_position = list(character_initial_position)
character_color = BLUE
character_on_ground = True
character_gravity = 2
character_jump_power = 30
character_velocity = 0
character_rect = None