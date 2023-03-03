import pygame

pygame.init()

clk = pygame.time.Clock()

size = width, height = 256, 256
screen = pygame.display.set_mode(size)
background_image = pygame.image.load('./proyectos/snes/templates/control.png').convert()
frameReact = pygame.Rect((0, 0), (width, height))

crosshair = pygame.surface.Surface((10, 10))
pygame.draw.circle(crosshair, pygame.Color("white"), (5, 5), 10, 0)

crosshairb = pygame.surface.Surface((10, 10))
pygame.draw.circle(crosshairb, pygame.Color("red"), (5, 5), 5, 0)




while True:

    pygame.event.pump()

    screen.blit(background_image, (0,0))

    Keys=pygame.key.get_pressed()

    if Keys[pygame.K_a]: screen.blit(crosshair, (35, 122))#boton izq
    if Keys[pygame.K_a] and Keys[pygame.K_w]: screen.blit(crosshair, (35, 108))#boton izq-arriba
    if Keys[pygame.K_a] and Keys[pygame.K_s]: screen.blit(crosshair, (35, 135))#boton abajo-izq
    if Keys[pygame.K_d]: screen.blit(crosshair, (65, 122))#boton der
    if Keys[pygame.K_d] and Keys[pygame.K_w]: screen.blit(crosshair, (65, 108))#boton der-arriba
    if Keys[pygame.K_d] and Keys[pygame.K_s]: screen.blit(crosshair, (65, 135))#boton abajo-der
    if Keys[pygame.K_w]: screen.blit(crosshair, (49, 108))#boton arriba
    if Keys[pygame.K_s]: screen.blit(crosshair, (49, 135))#boton abajo

    if Keys[pygame.K_h]: screen.blit(crosshair, (196, 104))#boton x
    if Keys[pygame.K_j]: screen.blit(crosshair, (172, 121))#boton y
    if Keys[pygame.K_k]: screen.blit(crosshair, (220, 120))#boton a
    if Keys[pygame.K_l]: screen.blit(crosshair, (196, 142))#boton b

    if Keys[pygame.K_u]: screen.blit(crosshair, (50, 60))#gatillo izquierdo
    if Keys[pygame.K_i]: screen.blit(crosshair, (200, 60))#gatillo derecho
    if Keys[pygame.K_o]: screen.blit(crosshair, (100, 130))#select
    if Keys[pygame.K_p]: screen.blit(crosshair, (128, 130))#start

    x = -1 if Keys[pygame.K_LEFT] else 1 if Keys[pygame.K_RIGHT] else 0

    y = -1 if Keys[pygame.K_UP] else 1 if Keys[pygame.K_DOWN] else 0



    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            exit()


    screen.blit(crosshairb, ((x*20)+55-5, (y*20)+125-5))

    pygame.display.flip()

    clk.tick(40)