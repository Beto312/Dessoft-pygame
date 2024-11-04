import pygame

pygame.init()

largura = 900
altura = 775

window = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Fireboy and Watergirl')
telainicial = pygame.image.load("assets\img\inicial.png").convert()
rect = telainicial.get_rect()
imagem_fundo = pygame.transform.scale(telainicial,(largura, altura))


game = True
while game == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    window.fill((255,255,255))
    window.blit(imagem_fundo,rect) #fundo do jogo
    pygame.display.update()

    

pygame.quit()