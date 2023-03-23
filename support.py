import pygame
from settings import tiles_size
from csv import reader

def import_csv_layout(path):
    terrain_map = []
    with open(path) as map:
        level = reader(map,delimiter = ',')
        for row in level:
            terrain_map.append(list(row))
        return terrain_map
    
def import_cut_graphics(path):  #obtendo a lista de sprites
    surface = pygame.image.load(path).convert_alpha()
    tile_num_x = int(surface.get_size()[0] / tiles_size)   #descobrindo quantos ladrilho o eixo x possui
    tile_num_y = int(surface.get_size()[1] / tiles_size)   #descobrindo quantos ladrilho o eixo y possui
    
    cut_tiles = []
    for row in range(tile_num_y):
        for col in range(tile_num_x):
            x = col * tiles_size
            y = row * tiles_size
            new_surf = pygame.Surface((tiles_size,tiles_size),flags = pygame.SRCALPHA)  #criando ladrilho 32x32
            new_surf.blit(surface,(0,0),pygame.Rect(x,y,tiles_size,tiles_size)) #pecorrendo tiledset de 32x32 em 32x32
            cut_tiles.append(new_surf)

    return cut_tiles