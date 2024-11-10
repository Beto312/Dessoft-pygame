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

# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Define a aceleração da gravidade
GRAVITY = 0.5
# Define a velocidade inicial no pulo
JUMP_SIZE = TILE_SIZE * 0.35
# Define a velocidade em x
SPEED_X = 3.2

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

# Classe Jogador que representa o herói
class Player(pygame.sprite.Sprite):
    def __init__(self, player_img, row, column, blocks):
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

    def jump(self):
        if self.state == STILL:
            self.speedy -= JUMP_SIZE
            self.state = JUMPING

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







    return assets

# Função principal do jogo
# def game_screen(screen):
    # clock = pygame.time.Clock()
    # assets = load_assets(img_dir)
    # all_sprites = pygame.sprite.Group()
    # blocks = pygame.sprite.Group()
    # player = Player(assets['PLAYER_IMG'], 12, 2, blocks)
    # for row in range(len(MAP)):
    #     for column in range(len(MAP[row])):
    #         tile_type = MAP[row][column]
    #         if tile_type == 'TILE_CENTER':
    #             tile = Tile(assets[''TILE_CENTER'_IMG'], row, column)
    #             all_sprites.add(tile)
    #             blocks.add(tile)
    # all_sprites.add(player)
    # PLAYING = 0
    # DONE = 1
    # state = PLAYING
    # while state != DONE:
        # clock.tick(FPS)
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         state = DONE
        #     if event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_LEFT:
        #             player.speedx -= SPEED_X
        #             player.image = pygame.transform.flip(pygame.transform.scale(assets['PLAYER_IMG'], (PLAYER_WIDTH, PLAYER_HEIGHT)), True, False)
        #         elif event.key == pygame.K_RIGHT:
        #             player.speedx += SPEED_X
        #             player.image = pygame.transform.scale(assets['PLAYER_IMG'], (PLAYER_WIDTH, PLAYER_HEIGHT))
        #         elif event.key == pygame.K_UP or event.key == pygame.K_SPACE:
        #             player.jump()
        #     if event.type == pygame.KEYUP:
        #         if event.key == pygame.K_LEFT:
        #             player.speedx = 0
        #         elif event.key == pygame.K_RIGHT:
        #             player.speedx = 0
        # all_sprites.update()
        # screen.fill(BLACK)
        # all_sprites.draw(screen)
        # pygame.display.flip()

# Inicialização do Pygame.
# pygame.init()
# pygame.mixer.init()
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption(TITULO)
# print('*' * len(TITULO))
# print(TITULO.upper())
# print('*' * len(TITULO))
# print('Utilize as setas do teclado para andar e pular.')

# try:
#     game_screen(screen)
# finally:
#     pygame.quit()
