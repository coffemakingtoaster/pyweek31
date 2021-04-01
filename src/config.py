import pygame


WINDOW_HEIGHT = 720
WINDOW_WIDHT = 1280
FULLSCREEN = False


TILE_SIZE = 50
WINDOW_DIMENSIONS = (WINDOW_WIDHT, WINDOW_HEIGHT)
PLAYER_SPEED = 10


#controls
PLAYER_MOVE_UP = pygame.K_UP
PLAYER_MOVE_DOWN = pygame.K_DOWN
PLAYER_MOVE_LEFT = pygame.K_LEFT
PLAYER_MOVE_RIGHT = pygame.K_RIGHT
PLAYER_INTERACT = pygame.K_e


HOTKEY_1 = pygame.K_1

#TODO: This maybe in a data container for controls? ??? 

'''
This are the chances of the items. Therefore the sum of this has to be 1!
Currently (31/03/2021 - 20:53) the likeliness of drops is as follows:
coffee>donut>coin>jammer
'''
ITEM_COIN_CHANCE = 0.2
ITEM_DONUT_CHANCE = 0.3
ITEM_COFFEE_CHANCE = 0.4
ITEM_JAMMER_CHANCE = 0.1




ITEM_COFFEE_DURATION = 10
ITEM_COFFEE_SPEED = 15


DEBUG_DRAW_COLLISION = False