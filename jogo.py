import pygame
from general_helpers import *
from maps import *

pygame.init()

# Adicionar música de fundo
pygame.mixer.music.load("assets/music/Pixel 9.mp3")  
pygame.mixer.music.set_volume(0.5)  
pygame.mixer.music.play(-1)  

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

telaprincipal = pygame.image.load("assets/img/Background.png").convert()
rect = telaprincipal.get_rect()

img_fundo_jogo = pygame.transform.scale(telaprincipal,(largura, altura))

# configurações do botão:
corbotao = (0, 255, 0)
botao_x = largura // 2 - 115  #posição horizontal do botão
botao_y = altura // 2 + 240   #posição vertical do botão
botao_larg = 250   #largura
botao_h = 70    #altura 
fonte = pygame.font.Font(None, 40)
texto_botao = fonte.render("Start Game", True, (255, 255, 255))
game_state = 'inicial'


clock = pygame.time.Clock()
start_ticks = 0

# Define o caminho para as pastas de assets e imagens.
base_dir = path.dirname(__file__)
assets_dir = path.join(base_dir, 'assets')
img_dir = path.join(assets_dir, 'img')
assets = load_assets(img_dir)

paused = False
keep_game_open = True
level_is_setup = 0
current_level = 1

while keep_game_open == True:
    if game_state == 'inicial':
        for event in pygame.event.get():
            keep_game_open = handle_close_window_events(event, keep_game_open)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # se o mouse estiver entre a pos. horizontal e largura, se o mouse estiver entre a pos. vertical e altura, tela_atual == True
                if botao_x <= mouse_x <= botao_x + botao_larg and botao_y <= mouse_y <= botao_y + botao_h and game_state:
                    game_state = "Fase"

            # Botão
            pygame.draw.rect(window, corbotao, (botao_x, botao_y, botao_larg, botao_h))
            window.blit(texto_botao, (botao_x + 50, botao_y + 10))

            # Imagem na frente do botão
            window.fill((255, 255, 255))
            window.blit(img_fundo, rect)

    elif game_state == "Fase": 
        if not level_is_setup:
            all_sprites, player, player2 = level_setup(window, assets, MAPS[current_level])
            level_is_setup = 1

        if paused == False:
            clock.tick(FPS)
            seconds = (pygame.time.get_ticks() - start_ticks) // 1000

            for event in pygame.event.get():

                keep_game_open = handle_close_window_events(event, keep_game_open)
                paused = handle_pause_event(event, paused)

                player.handle_movement(event)
                player2.handle_movement(event)

            all_sprites.update()
            window.fill(BLACK)
            window.blit(img_fundo_jogo, rect)

            player_is_on_portal = player.handle_portal_interaction()
            player2_is_on_portal = player2.handle_portal_interaction()

            if not (player.alive and player2.alive):
                draw_gameover_screen(window, tela_gameover)
                pygame.time.delay(2000)
                level_is_setup = 0
                
            all_sprites.draw(window)

            player.dangers.draw(window)
            player2.dangers.draw(window)

            # cronômetro
            texto_tempo = fonte.render(f"Tempo: {seconds}s", True, (255, 255, 255))
            window.blit(texto_tempo, (10, 10))
            pygame.display.flip()

            if player_is_on_portal and player2_is_on_portal:

                # Trigger fade animation
                fade(window)

                # Show "Next Level!" popup
                show_next_level_popup(window)

                level_is_setup = 0

                game_state = "Mudar Fase"

        elif paused == True:
            draw_pause_screen(window, tela_pause)
            for event in pygame.event.get():

                keep_game_open = handle_close_window_events(event, keep_game_open)

                paused = handle_pause_event(event, paused)
    
    elif game_state == "Mudar Fase":
        show_next_level_popup(window)

        for event in pygame.event.get():
            keep_game_open = handle_close_window_events(event, keep_game_open)

            paused = handle_pause_event(event, paused)

            if (event.type == pygame.MOUSEBUTTONDOWN):
                # mouse_x, mouse_y = pygame.mouse.get_pos()
                # # se o mouse estiver entre a pos. horizontal e largura, se o mouse estiver entre a pos. vertical e altura, tela_atual == True
                # if botao_x <= mouse_x <= botao_x + botao_larg and botao_y <= mouse_y <= botao_y + botao_h and game_state:
                current_level += 1
                
                game_state = "Fase"
            
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_KP_ENTER, pygame.K_SPACE]:
                    current_level += 1

                    game_state = "Fase"
    
    elif game_state == "Credits":
        show_next_level_popup(window)

        for event in pygame.event.get():
            keep_game_open = handle_close_window_events(event, keep_game_open)

            paused = handle_pause_event(event, paused)

            if (event.type == pygame.MOUSEBUTTONDOWN):
                # mouse_x, mouse_y = pygame.mouse.get_pos()
                # # se o mouse estiver entre a pos. horizontal e largura, se o mouse estiver entre a pos. vertical e altura, tela_atual == True
                # if botao_x <= mouse_x <= botao_x + botao_larg and botao_y <= mouse_y <= botao_y + botao_h and game_state:
                current_level += 1
                
                game_state = "Fase"
            
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_KP_ENTER, pygame.K_SPACE]:
                    current_level += 1

                    game_state = "Fase"

    pygame.display.update()

pygame.quit()