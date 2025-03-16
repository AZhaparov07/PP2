import pygame
import time
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
background = pygame.image.load("mickeyclock.png")
minute_hand = pygame.image.load("rightmin_hand.png").convert_alpha()
second_hand = pygame.image.load("leftsec_hand.png").convert_alpha()
center_x, center_y = width // 2, height // 2
minute_pivot = (center_x ,  center_y ) 
second_pivot = (center_x ,  center_y )
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    current_time = time.localtime()
    minute_angle = -6 * current_time.tm_min
    second_angle = -6 * current_time.tm_sec
    rotated_minute_hand = pygame.transform.rotate(minute_hand, minute_angle)
    rotated_minute_rect = rotated_minute_hand.get_rect(center=minute_pivot)
    rotated_second_hand = pygame.transform.rotate(second_hand, second_angle)
    rotated_second_rect = rotated_second_hand.get_rect(center=second_pivot)
    screen.blit(background, (0, 0))
    screen.blit(rotated_minute_hand, rotated_minute_rect.topleft)
    screen.blit(rotated_second_hand, rotated_second_rect.topleft)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
