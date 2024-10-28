import pygame 

background_color = (0,0,0)

screen = pygame.display.set_mode((300,300))

pygame.display.set_caption("enclosed")
screen.fill(background_color)
pygame.display.flip()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False