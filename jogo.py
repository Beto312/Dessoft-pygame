import pygame
from mapa import *

pygame.init()

# Adicionar música de fundo
pygame.mixer.music.load("assets/music/Pixel 9.mp3")  # Substitua pelo caminho do arquivo de áudio
pygame.mixer.music.set_volume(0.5)  # Ajusta o volume (0.0 a 1.0)
pygame.mixer.music.play(-1)  # -1 faz a música tocar em loo

largura = 1080
altura = 720

window = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Fireboy and Watergirl')
telainicial = pygame.image.load("assets/img/fireboyandwatergirl.png").convert()
rect = telainicial.get_rect()
img_fundo = pygame.transform.scale(telainicial,(largura, altura))
tela_pause = pygame.image.load("assets/img/pause_foto.png").convert()
tela_pause = pygame.transform.scale(tela_pause, (largura, altura))
tela_gameover = pygame.image.load("assets/img/GAMEOVERpng.png").convert()
tela_gameover = pygame.transform.scale(tela_gameover, (largura, altura))

# configurações do botão:
corbotao = (0, 255, 0)
botao_x = largura // 2 - 115  #posição horizontal do botão
botao_y = altura // 2 + 240   #posição vertical do botão
botao_larg = 250   #largura
botao_h = 70    #altura 
fonte = pygame.font.Font(None, 40)
texto_botao = fonte.render("Start Game", True, (255, 255, 255))
tela_atual = 'inicial'


clock = pygame.time.Clock()
start_ticks = 0
assets = load_assets(img_dir)
all_sprites = pygame.sprite.Group()
blocks = pygame.sprite.Group()

# portais
fire_portal_pos = (930, 60)
fire_portal_pos2 = (930, 60)
water_portal_pos = (870, 60)
water_portal_pos2 = (870, 60)

# Crie retângulos para detectar as colisões
fire_portal_rect = assets['FIRE_PORTAL'].get_rect(topleft=fire_portal_pos)
fire_portal_rect2 = assets['FIRE_PORTAL2'].get_rect(topleft=fire_portal_pos2)
water_portal_rect = assets['WATER_PORTAL'].get_rect(topleft=water_portal_pos)
water_portal_rect2 = assets['WATER_PORTAL2'].get_rect(topleft=water_portal_pos2)

# diamantes de fogo - coordenadas
diamante = Diamantefire(600,420)
diamantef = Diamantefire(160,90)
diamantefi = Diamantefire(500,150)
diamantefir = Diamantefire(400,650)

# diamantes de água - coordenadas
diamante2 = Diamantewater(250,390)
diamante2w = Diamantewater(40,175)
diamante2wa = Diamantewater(350,150)
diamante2wat = Diamantewater(695,660)


diamantes = pygame.sprite.Group()
diamantes2 = pygame.sprite.Group()


diamantes.add(diamante)
diamantes.add(diamantef)
diamantes.add(diamantefi)
diamantes.add(diamantefir)
diamantes2.add(diamante2)
diamantes2.add(diamante2w)
diamantes2.add(diamante2wa)
diamantes2.add(diamante2wat)

player = Player(assets['PLAYER_IMG'], 50, 2, blocks, diamantes)
player2 = Player(assets['PLAYER_IMG2'], 20, 2, blocks, diamantes2)

for row in range(len(MAP)):
    for column in range(len(MAP[row])):
        tile_type = MAP[row][column]
        if tile_type in assets.keys():
            tile = Tile(assets[tile_type], row, column)
            all_sprites.add(tile)
            blocks.add(tile)

all_sprites.add(player)
all_sprites.add(player2)
all_sprites.add(diamante)
all_sprites.add(diamantef)
all_sprites.add(diamantefi)
all_sprites.add(diamantefir)
all_sprites.add(diamante2)
all_sprites.add(diamante2w)
all_sprites.add(diamante2wa)
all_sprites.add(diamante2wat)

telaprincipal = pygame.image.load("assets/img/Background.png").convert()
rect = telaprincipal.get_rect()
img_fundo_jogo = pygame.transform.scale(telaprincipal,(largura, altura))

PLAYING = 0
PAUSED = 1
state = PLAYING

# posição do fogo
fire_animation = assets['FIRE_ANIMATION']
fire_pos = [
    {"pos": (290, 673), "frame_index": 0},
    {"pos": (300, 673), "frame_index": 0},
    {"pos": (310, 673), "frame_index": 0},
    {"pos": (470, 430), "frame_index": 0},
    {"pos": (480, 430), "frame_index": 0},
    {"pos": (1030, 580),"frame_index": 0},
    {"pos": (660, 130),"frame_index": 0},
]

# posição da água
water_animation = assets['WATER_ANIMATION']
water_pos = [
    {"pos": (490, 673),"frame_index": 0},
    {"pos": (500, 673),"frame_index": 0},
    {"pos": (510, 673),"frame_index": 0},
    {"pos": (1030, 430),"frame_index": 0},
    {"pos": (20, 190), "frame_index": 0},
    {"pos": (200, 160), "frame_index": 0},
    {"pos": (210, 160), "frame_index": 0},
]
def draw_gameover_screen():
    window.fill((0, 0, 0))
    window.blit(tela_gameover, (0, 0))
    pygame.display.flip()
# Função para desenhar a tela de pausa
def draw_pause_screen():
    window.fill((0, 0, 0))
    window.blit(tela_pause, (0,0))
    pygame.display.flip()

game = True
while game == True:
    if tela_atual == 'inicial':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
            # se o mouse estiver entre a pos. horizontal e largura, se o mouse estiver entre a pos. vertical e altura, tela_atual == True
                if botao_x <= mouse_x <= botao_x + botao_larg and botao_y <= mouse_y <= botao_y + botao_h and tela_atual:
                    tela_atual = 'jogo'

        # botão
            pygame.draw.rect(window, corbotao, (botao_x, botao_y, botao_larg, botao_h))
            window.blit(texto_botao, (botao_x + 50, botao_y + 10))
        # imagem na frente do botão
            window.fill((255, 255, 255))
            window.blit(img_fundo, rect)

    elif tela_atual == 'jogo': 
        if state == PLAYING:
            clock.tick(FPS)
            seconds = (pygame.time.get_ticks() - start_ticks) // 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    draw_gameover_screen()
                    pygame.time.delay(2000)
                    game = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        state = PAUSED
                    elif event.key == pygame.K_LEFT:
                        player.speedx -= SPEED_X
                        player.image = pygame.transform.flip(pygame.transform.scale(assets['PLAYER_IMG'], (PLAYER_WIDTH, PLAYER_HEIGHT)), True, False)
                    elif event.key == pygame.K_RIGHT:
                        player.speedx += SPEED_X
                        player.image = pygame.transform.scale(assets['PLAYER_IMG'], (PLAYER_WIDTH, PLAYER_HEIGHT))
                    elif event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                        player.jump()
                    elif event.key == pygame.K_a:
                        player2.speedx -= SPEED_X
                        player2.image = pygame.transform.flip(pygame.transform.scale(assets['PLAYER_IMG2'], (PLAYER_WIDTH, PLAYER_HEIGHT)), True, False)
                    elif event.key == pygame.K_d:
                        player2.speedx += SPEED_X
                        player2.image = pygame.transform.scale(assets['PLAYER_IMG2'], (PLAYER_WIDTH, PLAYER_HEIGHT))
                    elif event.key == pygame.K_w:
                        player2.jump()
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        player.speedx = 0
                    elif event.key == pygame.K_a or event.key == pygame.K_d:
                        player2.speedx = 0

            all_sprites.update()
            window.fill(BLACK)
            window.blit(img_fundo_jogo, rect)
            # window.blit(assets['FIRE_PORTAL'],fire_portal_pos)
            # window.blit(assets['WATER_PORTAL'],water_portal_pos)
            if player.rect.colliderect(fire_portal_rect):
                window.blit(assets['FIRE_PORTAL2'], fire_portal_pos2)
            else:
                window.blit(assets['FIRE_PORTAL'], fire_portal_pos)

            if player2.rect.colliderect(water_portal_rect):
                window.blit(assets['WATER_PORTAL2'], water_portal_pos2)
            else:
                window.blit(assets['WATER_PORTAL'], water_portal_pos)
            if player.rect.colliderect(fire_portal_rect) and player2.rect.colliderect(water_portal_rect):
                pygame.time.delay(2000)
                game = False
            all_sprites.draw(window)

            # configurações do fogo
            for fire in fire_pos:
                fire["frame_index"] = (fire["frame_index"] + 1) % len(fire_animation)
                fire_image = fire_animation[fire["frame_index"]]
                window.blit(fire_image, fire["pos"])
                # Colisão do player2 com o fogo
                fire_rect = fire_image.get_rect(topleft=fire["pos"])

                if fire_rect.colliderect(player2.rect):
                    draw_gameover_screen()
                    pygame.time.delay(2000)
                    game = False

            # configurações da água
            for water in water_pos:
                water["frame_index"] = (water["frame_index"] + 1) % len(water_animation)
                water_image = water_animation[water["frame_index"]]
                window.blit(water_image, water["pos"])
                # Colisão do player com a água
                water_rect = water_image.get_rect(topleft=water["pos"])

                if water_rect.colliderect(player.rect):
                    draw_gameover_screen()
                    pygame.time.delay(2000)
                    game = False

            # cronômetro
            texto_tempo = fonte.render(f"Tempo: {seconds}s", True, (255, 255, 255))
            window.blit(texto_tempo, (10, 10))
            pygame.display.flip()


        elif state == PAUSED:
            draw_pause_screen()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        state = PLAYING
                    # elif event.key == pygame.K_r:
                    #     tela_atual = 'inicial'
                    #     state = PLAYING
                    #     start_ticks = pygame.time.get_ticks()  # Reinicia o tempo

    pygame.display.update()

pygame.quit()








# python
# Copy code
# import pygame
# from mapa import *

# pygame.init()

# largura = 1080
# altura = 720

# window = pygame.display.set_mode((largura, altura))
# pygame.display.set_caption('Fireboy and Watergirl')
# telainicial = pygame.image.load("assets/img/fireboyandwatergirl.png").convert()
# rect = telainicial.get_rect()
# img_fundo = pygame.transform.scale(telainicial, (largura, altura))

# # Configurações do botão:
# corbotao = (0, 255, 0)
# botao_x = largura // 2 - 115
# botao_y = altura // 2 + 280
# botao_larg = 250
# botao_h = 59
# fonte = pygame.font.Font(None, 40)
# texto_botao = fonte.render("Start Game", True, (255, 255, 255))
# tela_atual = 'inicial'

# clock = pygame.time.Clock()
# start_ticks = 0
# assets = load_assets(img_dir)
# all_sprites = pygame.sprite.Group()
# blocks = pygame.sprite.Group()

# # Criação dos diamantes de fogo e água
# diamantes = pygame.sprite.Group()
# diamantes2 = pygame.sprite.Group()

# # Adiciona os diamantes e outros sprites ao grupo
# diamante_positions = [(600, 420), (160, 90), (500, 150), (700, 660)]
# for pos in diamante_positions:
#     diamante = Diamantefire(*pos)
#     diamantes.add(diamante)
#     all_sprites.add(diamante)

# diamante2_positions = [(250, 390), (40, 175), (350, 150), (400, 660)]
# for pos in diamante2_positions:
#     diamante2 = Diamantewater(*pos)
#     diamantes2.add(diamante2)
#     all_sprites.add(diamante2)

# player = Player(assets['PLAYER_IMG'], 50, 2, blocks, diamantes)
# player2 = Player(assets['PLAYER_IMG2'], 20, 2, blocks, diamantes2)

# for row in range(len(MAP)):
#     for column in range(len(MAP[row])):
#         tile_type = MAP[row][column]
#         if tile_type in assets.keys():
#             tile = Tile(assets[tile_type], row, column)
#             all_sprites.add(tile)
#             blocks.add(tile)

# # Configuração de fundo
# telaprincipal = pygame.image.load("assets/img/Background.png").convert()
# rect = telaprincipal.get_rect()
# img_fundo_jogo = pygame.transform.scale(telaprincipal, (largura, altura))

# PLAYING = 0
# DONE = 1
# state = PLAYING

# # Adiciona a animação de fogo
# fire_animation = assets['FIRE_ANIMATION']
# fire_index = 0
# fire_pos = (450, 350)  # posição do fogo no jogo (exemplo)

# game = True
# while game:
#     if tela_atual == 'inicial':
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 game = False
#             elif event.type == pygame.MOUSEBUTTONDOWN:
#                 mouse_x, mouse_y = pygame.mouse.get_pos()
#                 if botao_x <= mouse_x <= botao_x + botao_larg and botao_y <= mouse_y <= botao_y + botao_h:
#                     tela_atual = 'jogo'

#         window.fill((255, 255, 255))
#         window.blit(img_fundo, rect)
#         pygame.draw.rect(window, corbotao, (botao_x, botao_y, botao_larg, botao_h))
#         window.blit(texto_botao, (botao_x + 50, botao_y + 10))

#     elif tela_atual == 'jogo':
#         clock.tick(30)

#         seconds = (pygame.time.get_ticks() - start_ticks) // 1000

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 game = False
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_LEFT:
#                     player.speedx -= SPEED_X
#                 elif event.key == pygame.K_RIGHT:
#                     player.speedx += SPEED_X
#                 elif event.key == pygame.K_UP or event.key == pygame.K_SPACE:
#                     player.jump()
#                 if event.key == pygame.K_a:
#                     player2.speedx -= SPEED_X
#                 elif event.key == pygame.K_d:
#                     player2.speedx += SPEED_X
#                 elif event.key == pygame.K_w:
#                     player2.jump()
#             if event.type == pygame.KEYUP:
#                 if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
#                     player.speedx = 0
#                 if event.key in [pygame.K_a, pygame.K_d]:
#                     player2.speedx = 0

#         all_sprites.update()
#         window.fill((0, 0, 0))
#         window.blit(img_fundo_jogo, rect)
#         all_sprites.draw(window)

#         # Atualizar animação de fogo
#         fire_index = (fire_index + 1) % len(fire_animation)
#         window.blit(fire_animation[fire_index], fire_pos)

#         # Colisão do player2 com o fogo
#         fire_rect = fire_animation[fire_index].get_rect(topleft=fire_pos)
#         if fire_rect.colliderect(player2.rect):
#             tela_atual = 'game_over'  # Troca a tela para fim de jogo
#             print("O player2 colidiu com o fogo e morreu.")

#         texto_tempo = fonte.render(f"Tempo: {seconds}s", True, (255, 255, 255))
#         window.blit(texto_tempo, (10,10))

#         pygame.display.flip()

#     pygame.display.update()

#     hits = pygame.sprite.spritecollide(player, diamantes, True)
#     hits2 = pygame.sprite.spritecollide(player2, diamantes2, True)

# pygame.quit()