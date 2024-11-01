import pygame 
import enclosed
import numpy

pygame.display.set_caption("enclosed")
#--------------------------------------------VALORES INIT
field = []
memory = []
player = enclosed.player_box(0,0,1,1)
gunplayer = enclosed.gun()
#--------------------------------------------INIMIGOS
alvo = enclosed.objct(11, -4)
alvo2 = enclosed.objct(6, -4)

field.append(alvo)
field.append(alvo2)
#--------------------------------------------
clock = pygame.time.Clock()

GREENPOS = 0

background_color = (0,0,0)
interface_color = (28, 27, 26)
screen = pygame.display.set_mode((300,300))

bg = pygame.image.load("BACKGROUND.png")
bg = pygame.transform.scale(bg, (300,300))
greenlit = pygame.image.load("greenlit.png")
greenlit = pygame.transform.scale(greenlit, (300,300))

def render_green_light(GREENPOS):
    if GREENPOS< 0 or GREENPOS > 180:
        GREENPOS = 400
    greenrect = pygame.Rect(GREENPOS, 0, 300, 300)
    screen.blit(greenlit, greenrect)

def calcular_angulo_relativo(detectado, player):
    ximportante, yimportante = detectado.position[0] - player.position[0],  detectado.position[1] - player.position[1]
    angleimportante = numpy.degrees(numpy.arcsin(ximportante/(numpy.sqrt(ximportante**2+yimportante**2))))
    return angleimportante
#pygame.draw.rect(screen, interface_color, pygame.Rect(0,0,150,150))


running = True

while running:
    for event in pygame.event.get():
        screen.fill(background_color)
        rect = pygame.Rect(0,0,300,300)
        screen.blit(bg, rect)
        for detectado in memory:
            angulocalculado = calcular_angulo_relativo(detectado, player) + player.orientation
            render_green_light(angulocalculado)
        pygame.display.flip()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_u:
                memory = enclosed.detect_things(player.position, field)
                print(memory)
            if event.key == pygame.K_a:
                player.rotate(10)
            if event.key == pygame.K_d:
                player.rotate(-10)
        if event.type == pygame.QUIT:
            running = False
    clock.tick(10)  # limits FPS to 10
