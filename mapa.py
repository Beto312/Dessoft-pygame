# -*- coding: utf-8 -*-

# Importando as bibliotecas necessárias.
import pygame
from os import path

# Define o caminho para as pastas de assets e imagens.
base_dir = path.dirname(__file__)
assets_dir = path.join(base_dir, 'assets')
img_dir = path.join(assets_dir, 'img')

# Dados gerais do jogo.
TITULO = 'Exemplo de Pulo com obstáculos'
WIDTH = 1080  # Largura da tela
HEIGHT = 720  # Altura da tela
TILE_SIZE = 30  # Tamanho de cada tile (cada tile é um quadrado)
PLAYER_WIDTH = TILE_SIZE * 0.8
PLAYER_HEIGHT = int(TILE_SIZE * 1.5)
FPS = 60  # Frames por segundo

#define as imagens dos diamantes
firediamante_img = pygame.image.load("assets/img/1.png")
firediamante_img = pygame.transform.scale(firediamante_img, (25, 25))

waterdiamante_img = pygame.image.load("assets/img/8.png")
waterdiamante_img = pygame.transform.scale(waterdiamante_img, (25, 25))





# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Define a aceleração da gravidade
GRAVITY = 0.60
# Define a velocidade inicial no pulo
JUMP_SIZE = TILE_SIZE * 0.41
# Define a velocidade em x
SPEED_X = 3.6

# Define os tipos de tiles
BLOCK = 0
EMPTY = -1

# Define o mapa com os tipos de tiles
MAP = [
    
    ['TILE_POINT_DOWN_LEFT', 'TILE_BOTTOM', 'TILE_BOTTOM', 'TILE_BOTTOM', 'TILE_BOTTOM', 'TILE_BOTTOM', 'TILE_BOTTOM', 'TILE_BOTTOM', 'TILE_BOTTOM', 'TILE_BOTTOM', 'TILE_BOTTOM', 'TILE_BOTTOM', 'TILE_BOTTOM', 'TILE_BOTTOM', 'TILE_BOTTOM', 'TILE_BOTTOM', 'TILE_BOTTOM', 'TILE_BOTTOM', 'TILE_BOTTOM', 'TILE_BOTTOM', 'TILE_BOTTOM', 'TILE_BOTTOM', 'TILE_BOTTOM', 'TILE_BOTTOM', 'TILE_BOTTOM', 'TILE_BOTTOM', 'TILE_BOTTOM', 'TILE_BOTTOM', 'TILE_BOTTOM', 'TILE_BOTTOM', 'TILE_BOTTOM', 'TILE_BOTTOM', 'TILE_BOTTOM', 'TILE_BOTTOM', 'TILE_BOTTOM', 'TILE_POINT_DOWN_RIGHT'],
    ['TILE_RIGHT', EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, 'TILE_LEFT'],
    ['TILE_RIGHT', EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, 'TILE_LEFT'],
    ['TILE_RIGHT', EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, 'TILE_LEFT'],
    ['TILE_RIGHT', EMPTY, EMPTY, EMPTY, EMPTY, 'TILE_TOP_LEFT', 'TILE_TOP_RIGHT', EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, 'TILE_TOP_LEFT', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_LEFT'],
    ['TILE_RIGHT', EMPTY, EMPTY, EMPTY, 'TILE_TOP_LEFT', 'TILE_POINT_UP_LEFT', 'TILE_RIGHT', EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, 'TILE_TOP_LEFT', 'TILE_POINT_UP_LEFT', 'TILE_CENTER', 'TILE_CENTER', 'TILE_CENTER', 'TILE_CENTER', 'TILE_CENTER', 'TILE_CENTER', 'TILE_CENTER', 'TILE_CENTER', 'TILE_CENTER', 'TILE_CENTER', 'TILE_CENTER', 'TILE_LEFT'],
    ['TILE_RIGHT', EMPTY, EMPTY, EMPTY, EMPTY, 'TILE_CENTER', 'TILE_POINT_UP_RIGHT', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_POINT_UP_LEFT', 'TILE_CENTER', EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, 'TILE_LEFT'],
    ['TILE_RIGHT', 'TILE_TOP', 'TILE_TOP_RIGHT', EMPTY, EMPTY, 'TILE_CENTER', 'TILE_CENTER', 'TILE_CENTER', 'TILE_CENTER', 'TILE_CENTER', 'TILE_CENTER', 'TILE_CENTER', 'TILE_CENTER', 'TILE_CENTER', 'TILE_CENTER', 'TILE_CENTER', 'TILE_CENTER', 'TILE_CENTER', 'TILE_CENTER', 'TILE_CENTER', 'TILE_CENTER', 'TILE_CENTER', 'TILE_CENTER', 'TILE_CENTER', EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, 'TILE_LEFT'],
    ['TILE_RIGHT', 'TILE_CENTER', 'TILE_RIGHT', EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, 'TILE_CENTER', 'TILE_CENTER', 'TILE_CENTER', 'TILE_CENTER', 'TILE_CENTER', 'TILE_CENTER', 'TILE_CENTER', 'TILE_CENTER', 'TILE_CENTER', 'TILE_CENTER', 'TILE_CENTER', 'TILE_CENTER', 'TILE_CENTER', 'TILE_CENTER', 'TILE_CENTER', EMPTY, 'TILE_TOP_LEFT', 'TILE_TOP_RIGHT', EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, 'TILE_LEFT'],
    ['TILE_RIGHT', 'TILE_CENTER', 'TILE_POINT_UP_RIGHT', 'TILE_TOP_RIGHT', EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, 'TILE_LEFT', 'TILE_POINT_UP_RIGHT', 'TILE_TOP_RIGHT', EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, 'TILE_LEFT'],
    ['TILE_RIGHT', 'TILE_CENTER', 'TILE_CENTER', 'TILE_RIGHT', EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, 'TILE_LEFT', 'TILE_CENTER', 'TILE_RIGHT', EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, 'TILE_LEFT'],
    ['TILE_RIGHT', 'TILE_CENTER', 'TILE_CENTER', 'TILE_POINT_UP_RIGHT', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_POINT_UP_LEFT', 'TILE_CENTER', 'TILE_POINT_UP_RIGHT', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP_RIGHT', EMPTY, EMPTY, EMPTY, 'TILE_LEFT'],
    ['TILE_RIGHT', EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, 'TILE_POINT_UP_RIGHT', 'TILE_TOP_RIGHT', EMPTY, EMPTY, 'TILE_LEFT'],
    ['TILE_RIGHT', EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, 'TILE_LEFT'],
    ['TILE_RIGHT', EMPTY, EMPTY, 'TILE_TOP_LEFT', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP_RIGHT', EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, 'TILE_LEFT'],
    ['TILE_RIGHT', EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, 'TILE_POINT_UP_RIGHT', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_LEFT'],
    ['TILE_RIGHT', EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, 'TILE_LEFT'],
    ['TILE_RIGHT', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP_RIGHT', EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, 'TILE_LEFT'],
    ['TILE_RIGHT', EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, 'TILE_POINT_UP_RIGHT', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP_RIGHT', EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, 'TILE_LEFT'],
    ['TILE_RIGHT', EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, 'TILE_POINT_UP_RIGHT', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP_RIGHT', EMPTY, EMPTY, EMPTY, 'TILE_LEFT'],
    ['TILE_RIGHT', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP_RIGHT', EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, 'TILE_TOP_LEFT', 'TILE_LEFT'],
    ['TILE_RIGHT', EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, 'TILE_TOP_LEFT', 'TILE_POINT_UP_LEFT', 'TILE_LEFT'],
    ['TILE_RIGHT', EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, 'TILE_LEFT', 'TILE_CENTER', 'TILE_LEFT'],
    ['TILE_POINT_UP_RIGHT', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_TOP', 'TILE_POINT_UP_LEFT'],
]
# Define estados possíveis do jogador
STILL = 0
JUMPING = 1
FALLING = 2

# Classe que representa os blocos do cenário
class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_img, row, column):
        pygame.sprite.Sprite.__init__(self)
        tile_img = pygame.transform.scale(tile_img, (TILE_SIZE, TILE_SIZE))
        self.image = tile_img
        self.rect = self.image.get_rect()
        self.rect.x = TILE_SIZE * column
        self.rect.y = TILE_SIZE * row

# Classe que representa os diamantes do fireboy
class Diamantefire(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = firediamante_img
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def collect(self, player):
        return player.character == 'player'

# Classe que representa os diamantes da watergitl
class Diamantewater(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = waterdiamante_img
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def collect(self, player):
        return player.character == 'player2'

# Classe Jogador que representa o herói
class Player(pygame.sprite.Sprite):
    def __init__(self, player_img, row, column, blocks,diamantes):
        pygame.sprite.Sprite.__init__(self)
        self.state = STILL
        player_img = pygame.transform.scale(player_img, (PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image = player_img
        self.rect = self.image.get_rect()
        self.blocks = blocks
        self.rect.x = column * TILE_SIZE
        self.rect.bottom = row * TILE_SIZE
        self.speedx = 0
        self.speedy = 0
        self.diamantes = diamantes
        self.score = 0

    def update(self):
        self.speedy += GRAVITY
        if self.speedy > 0:
            self.state = FALLING
        self.rect.y += self.speedy
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        collisions = pygame.sprite.spritecollide(self, self.blocks, False)
        for collision in collisions:
            if self.speedy > 0:
                self.rect.bottom = collision.rect.top
                self.speedy = 0
                self.state = STILL
            elif self.speedy < 0:
                self.rect.top = collision.rect.bottom
                self.speedy = 0
                self.state = STILL
        self.rect.x += self.speedx
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right >= WIDTH:
            self.rect.right = WIDTH - 1
        collisions = pygame.sprite.spritecollide(self, self.blocks, False)
        for collision in collisions:
            if self.speedx > 0:
                self.rect.right = collision.rect.left
            elif self.speedx < 0:
                self.rect.left = collision.rect.right

        d_coletados = pygame.sprite.spritecollide(self, self.diamantes, True)
        if d_coletados:
            self.score += len(d_coletados)  
            print(f"Pontuação: {self.score}")

    def jump(self):
        if self.state == STILL:
            self.speedy -= JUMP_SIZE
            self.state = JUMPING

#  Classe que representa a animação do fogo
class Fire(pygame.sprite.Sprite): 
    def __init__(self, x, y, fireanimation_frames): 
        super().__init__() 
        self.animation_frames = fireanimation_frames 
        self.current_frame = 0 
        self.image = self.animation_frames[self.current_frame] 
        self.rect = self.image.get_rect() 
        self.rect.topleft = (x, y)
        self.animation_speed = 0.15 
        self.animation_timer = 0

    def update(self):
        self.animation_timer += self.animation_speed 
        if self.animation_timer >= 1: 
            self.animation_timer = 0 
            self.current_frame = (self.current_frame + 1) % len(self.animation_frames) 
            self.image = self.animation_frames[self.current_frame]

# Função para carregar todos os assets de uma vez
def load_assets(img_dir):
    assets = {}
    assets['PLAYER_IMG'] = pygame.image.load(path.join(img_dir, 'Fireboy.png')).convert_alpha()
    assets['PLAYER_IMG2'] = pygame.image.load(path.join(img_dir, 'watergirl.png')).convert_alpha()
    assets['BLOCK_IMG'] = pygame.image.load(path.join(img_dir, 'pedra.jpg')).convert()
    assets['BACKGROUND_IMG'] = pygame.image.load(path.join(img_dir, 'Background.png')).convert()
    assets['TILE_CENTER'] = pygame.image.load(path.join(img_dir, 'Tile_12.png')).convert()
    assets['TILE_TOP'] = pygame.image.load(path.join(img_dir, 'Tile_02.png')).convert()
    assets['TILE_BOTTOM'] = pygame.image.load(path.join(img_dir, 'Tile_05.png')).convert()
    assets['TILE_LEFT'] = pygame.image.load(path.join(img_dir, 'Tile_11.png')).convert()
    assets['TILE_TOP_LEFT'] = pygame.image.load(path.join(img_dir, 'Tile_01.png')).convert()
    assets['TILE_TOP_RIGHT'] = pygame.image.load(path.join(img_dir, 'Tile_03.png')).convert()
    assets['TILE_EDGE_LEFT'] = pygame.image.load(path.join(img_dir, 'Tile_48.png')).convert()
    assets['TILE_EDGE_RIGHT'] = pygame.image.load(path.join(img_dir, 'Tile_47.png')).convert()
    assets['TILE_RIGHT'] = pygame.image.load(path.join(img_dir, 'Tile_14.png')).convert()
    assets['TILE_BOTTOM_LEFT'] = pygame.image.load(path.join(img_dir, 'Tile_21.png')).convert()
    assets['TILE_BOTTOM_RIGHT'] = pygame.image.load(path.join(img_dir, 'Tile_23.png')).convert()
    assets['TILE_POINT_UP_RIGHT'] = pygame.image.load(path.join(img_dir, 'Tile_24.png')).convert()
    assets['TILE_POINT_UP_LEFT'] = pygame.image.load(path.join(img_dir, 'Tile_57.png')).convert()
    assets['TILE_POINT_DOWN_RIGHT'] = pygame.image.load(path.join(img_dir, 'Tile_06.png')).convert()
    assets['TILE_POINT_DOWN_LEFT'] = pygame.image.load(path.join(img_dir, 'Tile_04.png')).convert()
    assets['TILE_POINT_UP_LEFT_DOWN_RIGHT'] = pygame.image.load(path.join(img_dir, 'Tile_19.png')).convert()
    assets['TILE_POINT_UP_RIGHT_DOWN_LEFT'] = pygame.image.load(path.join(img_dir, 'Tile_29.png')).convert()
    assets['FIRE_PORTAL'] = pygame.image.load(path.join(img_dir, 'door1.png')).convert_alpha()
    assets['FIRE_PORTAL2'] = pygame.image.load(path.join(img_dir, 'door2.png')).convert_alpha()
    assets['WATER_PORTAL'] = pygame.image.load(path.join(img_dir, 'door3.png')).convert_alpha()
    assets['WATER_PORTAL2'] = pygame.image.load(path.join(img_dir, 'door4.png')).convert_alpha()

    # Carregar as imagens de animação de fogo
    fireanimation_frames = []
    for i in range(0, 48):
        frame_path = path.join(img_dir, f'flame_{i}.png')  # Ajustado para flame_0.png até flame_48.png
        frame = pygame.image.load(frame_path).convert_alpha()
        frame = pygame.transform.scale(frame, (30, 30))
        fireanimation_frames.append(frame)
    assets['FIRE_ANIMATION'] = fireanimation_frames


    return assets
