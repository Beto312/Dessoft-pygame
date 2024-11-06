import pygame
from chat import *

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
botao_x = largura // 2 - 115 #posição horizontal do botão
botao_y = altura // 2 + 240   #posição vertical do botão
botao_larg = 250  # largura
botao_h = 59   # altura 
fonte = pygame.font.Font(None, 40)
texto_botao = fonte.render("Start Game", True, (255, 255, 255))
tela_atual = 'inicial'


clock = pygame.time.Clock()
assets = load_assets(img_dir)
all_sprites = pygame.sprite.Group()
blocks = pygame.sprite.Group()
player = Player(assets['PLAYER_IMG'], 12, 2, blocks)
for row in range(len(MAP)):
    for column in range(len(MAP[row])):
        tile_type = MAP[row][column]
        if tile_type == BLOCK:
            tile = Tile(assets['BLOCK_IMG'], row, column)
            all_sprites.add(tile)
            blocks.add(tile)
all_sprites.add(player)
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
            # se o maouse estiver entre a pos. horizontal e largura, se o mouse estiver entre a pos. vertical e altura, tela_atual == True
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
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.speedx = 0
                elif event.key == pygame.K_RIGHT:
                    player.speedx = 0
        all_sprites.update()
        window.fill(BLACK)
        all_sprites.draw(window)
        pygame.display.flip()

    pygame.display.update()

pygame.quit()