import pygame 
pygame.display.set_caption("enclosed")

clock = pygame.time.Clock()

GREENPOS = 0

background_color = (0,0,0)
interface_color = (28, 27, 26)
screen = pygame.display.set_mode((300,300))

bg = pygame.image.load("BACKGROUND.png")
bg = pygame.transform.scale(bg, (300,300))
greenlit = pygame.image.load("greenlit.png")
greenlit = pygame.transform.scale(greenlit, (300,300))



#pygame.draw.rect(screen, interface_color, pygame.Rect(0,0,150,150))


running = True

while running:
    for event in pygame.event.get():
        screen.fill(background_color)
        rect = pygame.Rect(0,0,300,300)
        #GREENPOS += 1
        greenrect = pygame.Rect(GREENPOS, 0, 300, 300)
        screen.blit(bg, rect)
        screen.blit(greenlit, greenrect)

        pygame.display.flip()
        if event.type == pygame.QUIT:
            running = False
    clock.tick(10)  # limits FPS to 10
