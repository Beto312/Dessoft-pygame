import pygame

pygame.init()

info = pygame.display.Info()
window = pygame.display.set_mode((info.current_w, info.current_h))
pygame.display.set_caption('Fireboy and Watergirl')

game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    window.fill((255, 255, 255))  # fundo branco
    pygame.display.update()

pygame.quit()