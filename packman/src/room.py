import pygame
from src import consts
from src.wall import Wall


def setupRoom(all_sprites_list):
    wall_list = pygame.sprite.RenderPlain()
    for item in consts.walls:
        wall = Wall(item[0], item[1], item[2], item[3], consts.blue)
        wall_list.add(wall)
        all_sprites_list.add(wall)

    return wall_list
