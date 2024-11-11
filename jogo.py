import pygame
from mapa import *

pygame.init()

largura = 1080
altura = 720

window = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Fireboy and Watergirl')
telainicial = pygame.image.load("assets/img/fireboyandwatergirl.png").convert()
rect = telainicial.get_rect()
img_fundo = pygame.transform.scale(telainicial,(largura, altura))

# configurações do botão:
corbotao = (0, 255, 0)
botao_x = largura // 2 - 115  #posição horizontal do botão
botao_y = altura // 2 + 280   #posição vertical do botão
botao_larg = 250   #largura
botao_h = 59    #altura 
fonte = pygame.font.Font(None, 40)
texto_botao = fonte.render("Start Game", True, (255, 255, 255))
tela_atual = 'inicial'


clock = pygame.time.Clock()
start_ticks = 0
assets = load_assets(img_dir)
all_sprites = pygame.sprite.Group()
blocks = pygame.sprite.Group()

diamante = Diamantefire(600,150)
diamantef = Diamantefire(650,150)
diamantefi = Diamantefire(500,150)
diamantefir = Diamantefire(550,680)

diamante2 = Diamantewater(250,150)
diamante2w = Diamantewater(300,150)
diamante2wa = Diamantewater(350,150)
diamante2wat = Diamantewater(200,680)


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
DONE = 1
state = PLAYING

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
        clock.tick(FPS)
        
        # Calcula o tempo em segundos desde o início do jogo
        seconds = (pygame.time.get_ticks() - start_ticks) // 1000


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.speedx -= SPEED_X
                    player.image = pygame.transform.flip(pygame.transform.scale(assets['PLAYER_IMG'], (PLAYER_WIDTH, PLAYER_HEIGHT)), True, False)
                elif event.key == pygame.K_RIGHT:
                    player.speedx += SPEED_X
                    player.image = pygame.transform.scale(assets['PLAYER_IMG'], (PLAYER_WIDTH, PLAYER_HEIGHT))
                elif event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                    player.jump()
                if event.key == pygame.K_a:
                    player2.speedx -= SPEED_X
                    player2.image = pygame.transform.flip(pygame.transform.scale(assets['PLAYER_IMG2'], (PLAYER_WIDTH, PLAYER_HEIGHT)), True, False)
                elif event.key == pygame.K_d:
                    player2.speedx += SPEED_X
                    player2.image = pygame.transform.scale(assets['PLAYER_IMG2'], (PLAYER_WIDTH, PLAYER_HEIGHT))
                elif event.key == pygame.K_w:
                    player2.jump()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.speedx = 0
                elif event.key == pygame.K_RIGHT:
                    player.speedx = 0
                if event.key == pygame.K_a:
                    player2.speedx = 0
                elif event.key == pygame.K_d:
                    player2.speedx = 0
        all_sprites.update()
        window.fill(BLACK)
        window.blit(img_fundo_jogo, rect)
        all_sprites.draw(window)
        texto_tempo = fonte.render(f"Tempo: {seconds}s", True, (255, 255, 255))
        window.blit(texto_tempo, (10,10))

        pygame.display.flip()

    pygame.display.update()

    hits = pygame.sprite.spritecollide(player, diamantes, True)
    hits2 = pygame.sprite.spritecollide(player2, diamantes2, True)

pygame.quit()