import pygame
from support import import_csv_layout,import_cut_graphics
from settings import tiles_size
from tiles import Tile, StaticTile

class Level:
    def __init__(self,level_data,surface):
        self.display_surface = surface
        
        terrain_layout = import_csv_layout(level_data['terrain'])
        self.terrain_sprites = self.create_tile_group(terrain_layout, 'terrain')
        
    #percorre as linhas do mapa e as númera
    def create_tile_group(self,layout,type):
        sprite_group = pygame.sprite.Group()
         
        for row_index, row in enumerate(layout):    #lendo linha por linha do level_map horizontal
            for col_index, val in enumerate(row):   #lendo colunas na vertical
                if val != '-1':
                    x = col_index * tiles_size  #obtendo a posição de x
                    y = row_index * tiles_size  #obtendo a posição de y
            
                   
                    if type == 'terrain':
                        terrain_tile_list = []
                        for i in range(1,81):
                                terrain_tile_list = import_cut_graphics(f'graphics/terrain/IndustrialTile_{i}.png') #criando lista de sprites
                                tile_surface = terrain_tile_list[int(val)]
                                sprite = StaticTile(tiles_size,x,y,tile_surface) #criando sprite
                             
                        sprite_group.add(sprite)
                        
        return sprite_group
        
    def run(self):
        self.terrain_sprites.draw(self.display_surface)