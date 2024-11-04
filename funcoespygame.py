import pygame

pygame.init()

window = pygame.display.set_mode((900, 600))
pygame.display.set_caption('Fireboy and Watergirl')


game = True
while game == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    window.fill((255,255,255)) #fundo branco
    pygame.display.update()

pygame.quit()