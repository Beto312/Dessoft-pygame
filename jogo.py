import pygame

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
inicial_ativa = True

game = True
while game == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
        # se o maouse estiver entre a pos. horizontal e largura, se o mouse estiver entre a pos. vertical e altura, inicial_ativa == True
            if botao_x <= mouse_x <= botao_x + botao_larg and botao_y <= mouse_y <= botao_y + botao_h and inicial_ativa:
                inicial_ativa = False

    if inicial_ativa:
    # botão
        pygame.draw.rect(window, corbotao, (botao_x, botao_y, botao_larg, botao_h))
        window.blit(texto_botao, (botao_x + 50, botao_y + 10))
    # imagem na frente do botão
        window.fill((255, 255, 255))
        window.blit(img_fundo, rect)

    else: 
        window.blit(img_fundo,rect) #fundo do jogo

    pygame.display.update()

pygame.quit()