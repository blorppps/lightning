import pygame
import lightning
pygame.init()

screen = pygame.display.set_mode((1200,600))
clock = pygame.time.Clock()
running = True

lightning1 = lightning.lightning((200,200),30,20,10,10,2,screen,(0,255,255),2)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255,255,255))

    lightning.render(lightning1)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
