# -*- coding: utf-8 -*-

# Importando as bibliotecas necessárias.
import pygame
from os import path

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
SPEED_X = 4.5

# Define estados possíveis do jogador
STILL = 0
JUMPING = 1
FALLING = 2

# Classe que representa os sprites estaticos
class staticSprite(pygame.sprite.Sprite):
    def __init__(self, image, row, column, size=(1, 1)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(image, (TILE_SIZE * size[0], TILE_SIZE * size[1]))
        self.rect = self.image.get_rect()
        self.rect.x = TILE_SIZE * (column - size[0]//2)
        self.rect.y = TILE_SIZE * (row - size[1]//2)

class booleanAnimationSprite(pygame.sprite.Sprite):
    def __init__(self, window, static_sprite_0, static_sprite_1):
        self.window = window
        self.states = {
                            0: static_sprite_0,
                            1: static_sprite_1
        }
        self.state = 0

    def set_state(self, state):
        self.state = state

        self.show_in_current_state()

    def show_in_current_state(self):
        self.window.blit(self.get_img(self.state), self.get_rect(self.state))

    def get_img(self, state):
        return self.states[state].image
    
    def get_rect(self, state):
        return self.states[state].rect
    
class animatedSprite:#(pygame.sprite.Sprite):
    def __init__(self, animation_frames, row, column):
        # pygame.sprite.Sprite.__init__(self)
        self.animation_frames = animation_frames
        self.row = row
        self.column = column
        self.pos = (TILE_SIZE * column, TILE_SIZE * row)
        self.frame_index = 0
        # self.image = self.animation_frames[self.frame_index]
        # self.rect = self.image.get_rect()
    
    def next_frame(self):
        self.frame_index = (self.frame_index + 1) % len(self.animation_frames)
    
    def get_rect(self):
        return self.animation_frames[self.frame_index].rect
    
    def get_current_frame(self):
        return self.animation_frames[self.frame_index]
    
    def get_static_sprite(self):
        return staticSprite(self.animation_frames[self.frame_index], self.row, self.column)
    
    def render(self, window):
        window.blit(self.get_current_frame(), self.pos)
    
class animated_sprite_group:

    def __init__(self):
        self.animated_sprites = []
        self.sprite_group = pygame.sprite.Group()

    def add(self, animated_sprite):
        self.animated_sprites.append(animated_sprite)

    def draw(self, window):

        self.sprite_group = pygame.sprite.Group()

        for animated_sprite in self.animated_sprites:

            self.sprite_group.add(animated_sprite.get_static_sprite())

            animated_sprite.render(window)
            animated_sprite.next_frame()
            
    # def get_as_sprite_group(self):

    #     tmp = pygame.sprite.Group()

    #     for x in self.animated_sprites:
    #         tmp.get_static_sprite(x)

    #     return tmp


# Classe Jogador que representa o herói
# class Player(pygame.sprite.Sprite):
class Player(staticSprite):
    def __init__(self, window, player_type):
        self.state = STILL
        self.pointing = "R"
        self.player_type = player_type

        self.window = window

        self.speedx = 0
        self.speedy = 0
        self.score = 0
        
        self.diamantes = pygame.sprite.Group()
        self.blocks = pygame.sprite.Group()
        self.portals = pygame.sprite.Group()
        self.dangers = animated_sprite_group()

        self.control_jump = None
        self.control_left = None
        self.control_right = None

        self.alive = True

    def spawn_player(self, player_img, row, column):
        staticSprite.__init__(self, player_img, row, column, (0.8, 1.5))

    def set_controls(self, jump, left, right):
        self.control_jump = jump
        self.control_left = left
        self.control_right = right

    def update(self):
        
        self.update_physics()

        self.update_item_collection()

        self.update_damage()

    def update_damage(self):
        
        collisions = pygame.sprite.spritecollide(self, self.dangers.sprite_group, False)
        if collisions:
            self.alive = False

    def update_physics(self):

        self.speedy += GRAVITY
        if self.speedy > 0:
            self.state = FALLING
        
        self.rect.y += self.speedy
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        
        # Checks if on floor or ceiling
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

        # Keeps player in screen
        self.rect.x += self.speedx
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right >= WIDTH:
            self.rect.right = WIDTH - 1

        # Checks if against wall
        collisions = pygame.sprite.spritecollide(self, self.blocks, False)
        for collision in collisions:
            if self.speedx > 0:
                self.rect.right = collision.rect.left
            elif self.speedx < 0:
                self.rect.left = collision.rect.right

    def update_item_collection(self):
        d_coletados = pygame.sprite.spritecollide(self, self.diamantes, True)
        if d_coletados:
            self.score += len(d_coletados)  
            print(f"Pontuação: {self.score}")

    def jump(self):
        if self.state == STILL:
            self.speedy -= JUMP_SIZE
            self.state = JUMPING

    def handle_movement(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == self.control_left:
                self.speedx -= SPEED_X
                if self.pointing == "R":
                    self.pointing = "L"
                    self.image = pygame.transform.flip(self.image, True, False)#pygame.transform.scale(self.image, (PLAYER_WIDTH, PLAYER_HEIGHT)), True, False)
            elif event.key == self.control_right:
                self.speedx += SPEED_X
                if self.pointing == "L":
                    self.pointing = "R"
                    self.image = pygame.transform.flip(self.image, True, False)#pygame.transform.scale(self.image, (PLAYER_WIDTH, PLAYER_HEIGHT))
            elif event.key == self.control_jump:
                self.jump()
        elif event.type == pygame.KEYUP:
            if event.key == self.control_left or event.key == self.control_right:
                self.speedx = 0
    
    def handle_portal_interaction(self):

        self.portals.show_in_current_state()

        if self.rect.colliderect(self.portals.get_rect(0)):
            self.portals.set_state(1)
            return True
        else:
            self.portals.set_state(0)
            return False

def level_setup(window, assets, map):

    all_sprites = pygame.sprite.Group()

    player = Player(window, "FIRE")
    player.set_controls(pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT)
    # all_sprites.add(player)

    player2 = Player(window, "WATER")
    player2.set_controls(pygame.K_w, pygame.K_a, pygame.K_d)
    # all_sprites.add(player2)

    for row in range(len(map)):
        for column in range(len(map[row])):
            tile_type = map[row][column]
            
            if type(tile_type).__name__ == "str":
                if "TILE" in tile_type:
                    tile = staticSprite(assets[tile_type], row, column)
                    all_sprites.add(tile)
                    player.blocks.add(tile)
                    player2.blocks.add(tile)
                
                if "DIAMANTE" in tile_type:
                    object = staticSprite(assets[tile_type], row, column)
                    
                    if "FIRE" in tile_type:
                        player.diamantes.add(object)
                    if "WATER" in tile_type:
                        player2.diamantes.add(object)

                    all_sprites.add(object)
                
                if "PORTAL" in tile_type:
                    object = staticSprite(assets[tile_type], row, column, size=(2, 3))
                    object_2 = staticSprite(assets[f"{tile_type}2"], row, column, size=(2, 3))

                    if "FIRE" in tile_type:
                        player.portals = booleanAnimationSprite(window, object, object_2)

                    if "WATER" in tile_type:
                        player2.portals = booleanAnimationSprite(window, object, object_2)

                if "ANIMATION" in tile_type:
                    object = animatedSprite(assets[tile_type], row, column)

                    if "WATER" in tile_type:
                        player.dangers.add(object)
                    
                    if "FIRE" in tile_type:
                        player2.dangers.add(object)
                
                if "PLAYER" in tile_type:
                    # object = animatedSprite()

                    if "FIRE" in tile_type:
                        # player.dangers.add(object)
                        player.spawn_player(assets[tile_type], row, column)
                    
                    if "WATER" in tile_type:
                        # player2.dangers.add(object)
                        player2.spawn_player(assets[tile_type], row, column)\
                        
    all_sprites.add(player)
    all_sprites.add(player2)

    return all_sprites, player, player2

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

#  Classe que representa a animação da água
class Water(pygame.sprite.Sprite): 
    def __init__(self, x, y, wateranimation_frames): 
        super().__init__() 
        self.animation_frames = wateranimation_frames 
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

def fade(screen, color=(0, 0, 0), duration=1, size=(1080, 720)):
    fade_surface = pygame.Surface(size)
    fade_surface.fill(color)
    fade_surface.set_alpha(0)  # Start fully transparent
    clock = pygame.time.Clock()
    for alpha in range(0, 255, 5):  # Gradually increase alpha
        fade_surface.set_alpha(alpha)
        screen.blit(fade_surface, (0, 0))
        pygame.display.flip()
        clock.tick(60 // duration)  # Adjust speed with duration

def show_next_level_popup(screen, text="Next Level!", font_size=80, size=(1080, 720)):
    overlay = pygame.Surface(size, pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 128))  # Translucent background
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(size[0] // 2, size[1] // 2))
    screen.blit(overlay, (0, 0))
    screen.blit(text_surface, text_rect)
    pygame.display.flip()
    # pygame.time.delay(2000)  # Pause for 2 seconds

def restart_current_level(tela_atual, assets, all_sprites, blocks, diamantes, diamantes2, player, player2):

    all_sprites.empty()
    blocks.empty()
    diamantes.empty()
    diamantes2.empty()

    # Reload the current map
    current_map = MAPS[tela_atual]
    for row in range(len(current_map)):
        for column in range(len(current_map[row])):
            tile_type = current_map[row][column]
            if tile_type in assets.keys():
                tile = Tile(assets[tile_type], row, column)
                all_sprites.add(tile)
                blocks.add(tile)

    # Reposition players
    player.rect.topleft = (2 * TILE_SIZE, HEIGHT - TILE_SIZE * 2)
    player2.rect.topleft = (2 * TILE_SIZE, HEIGHT - TILE_SIZE * 5)
    all_sprites.add(player)
    all_sprites.add(player2)

    # Re-add diamonds (example positions)
    diamantes.add(staticSprite(300, 150), staticSprite(600, 420))
    diamantes2.add(Diamantewater(350, 150), Diamantewater(250, 390))
    all_sprites.add(*diamantes)
    all_sprites.add(*diamantes2)

def handle_close_window_events(event, game):
    
    # Quit the game
    if event.type == pygame.QUIT:
        game = False

    return game

def handle_pause_event(event, paused):
    
    # Pause the game
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_p:
            paused = not paused
    
    return paused

def draw_gameover_screen(window, tela_gameover):
    window.fill((0, 0, 0))
    window.blit(tela_gameover, (0, 0))
    pygame.display.flip()

# Função para desenhar a tela de pausa
def draw_pause_screen(window, tela_pause):
    window.fill((0, 0, 0))
    window.blit(tela_pause, (0,0))
    pygame.display.flip()