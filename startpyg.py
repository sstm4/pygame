import pygame,sys

pygame.init()
screenwidth = 800
screenheight = 600
screen = pygame.display.set_mode((screenwidth,screenheight))
pygame.display.set_caption("square")
bgcolour = (0, 204, 255)
charcolour = (255, 0, 0)

charsize = 50
charx = screenwidth // 2 - charsize // 2
chary = screenheight // 2 - charsize // 2
charspeed = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        chary -= charspeed
    if keys[pygame.K_s]:
        chary += charspeed
    if keys[pygame.K_a]:
        charx -= charspeed
    if keys[pygame.K_d]:
        charx += charspeed
    
    screen.fill((bgcolour))
    
    pygame.draw.rect(screen,charcolour,(charx,chary,charsize,charsize))
    
    
    pygame.display.flip()
    pygame.time.Clock().tick(60)
pygame.quit()
sys.exit()