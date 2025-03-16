import pygame
pygame.init()
width,height = 500, 500
screen =pygame.display.set_mode((width, height))
pygame.display.set_caption("moving ball")
ball_radius= 25
ball_x = width // 2
ball_y= height // 2
speed = 20
running = True
while running:
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255,0, 0), (ball_x,ball_y), ball_radius)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            running= False
        elif event.type== pygame.KEYDOWN:
            if event.key== pygame.K_UP and ball_y- ball_radius -speed >= 0:
                ball_y -= speed
            elif event.key == pygame.K_DOWN and ball_y  + ball_radius + speed <= height:
                ball_y += speed
            elif event.key== pygame.K_LEFT and ball_x- ball_radius - speed >= 0:
                ball_x -= speed
            elif event.key== pygame.K_RIGHT and ball_x + ball_radius + speed <= width:
                ball_x += speed
pygame.quit()