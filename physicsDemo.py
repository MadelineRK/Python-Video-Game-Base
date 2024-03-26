import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = pygame.Rect((300, 250, 50, 50))
gravity = 9.81
Dy = 0

run = True
while run:
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), player)

    key = pygame.key.get_pressed()
    if key[pygame. K_a] == True:
        player.move_ip(-1,0)
    elif key[pygame. K_d] == True:
        player.move_ip(1,0)
    elif key[pygame. K_w] == True:
        player.move_ip(0,-1)

    Dy += 9.81 * 0.001
    player.move_ip(0,Dy)

    if(player.y > 650):
        Dy *= -0.99
        player.y = 650
        player.move_ip(0,Dy)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()