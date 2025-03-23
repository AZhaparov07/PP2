import pygame
import random

WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Инициализация 
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

# Генерация случайной позиции еды
def get_random_food(snake):
    while True:
        x = random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE
        y = random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
        if (x, y) not in snake:
            return x, y

# Инициализация змейки
snake = [(WIDTH // 2, HEIGHT // 2)]
direction = (CELL_SIZE, 0)
food = get_random_food(snake)
score = 0
level = 1
speed = 10

running = True
while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, CELL_SIZE):
                direction = (0, -CELL_SIZE)
            elif event.key == pygame.K_DOWN and direction != (0, -CELL_SIZE):
                direction = (0, CELL_SIZE)
            elif event.key == pygame.K_LEFT and direction != (CELL_SIZE, 0):
                direction = (-CELL_SIZE, 0)
            elif event.key == pygame.K_RIGHT and direction != (-CELL_SIZE, 0):
                direction = (CELL_SIZE, 0)
    
    # Движение змейки
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    
    # Столкновение со стенами
    if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
        running = False
    
    # Столкновение с самой собой
    if new_head in snake:
        running = False
    
    snake.insert(0, new_head)
    
    # Поедание еды
    if new_head == food:
        score += 1
        food = get_random_food(snake)
        
        # Повышение уровня каждые 3 очка
        if score % 4 == 0:
            level += 1
            speed += 2  # Увеличение скорости
    else:
        snake.pop()
    
    # Змейка
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))
    
    # Еда
    pygame.draw.rect(screen, RED, (*food, CELL_SIZE, CELL_SIZE))
    
    # Счет и уровень
    font = pygame.font.Font(None, 30)
    score_text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    
    pygame.display.flip()
    clock.tick(speed)
    
pygame.quit()
