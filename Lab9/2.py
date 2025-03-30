import pygame
import random

# Параметры экрана
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Инициализация pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

# Класс еды 
class Food:
    def __init__(self, snake):
        self.respawn(snake)
        self.timer = random.randint(60, 180)  # Время еды (1-3 секунды)

    def respawn(self, snake):
        while True:
            self.x = random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE
            self.y = random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
            if (self.x, self.y) not in snake:
                break
        self.value = random.choice([1, 2, 5])  # Вес еды
        self.timer = random.randint(60, 180)  # Случайное время исчезновения (1-3 секунды)

    def update(self, snake):
        self.timer -= 1
        if self.timer <= 0:
            self.respawn(snake)

# Инициализация змейки
snake = [(WIDTH // 2, HEIGHT // 2)]
direction = (CELL_SIZE, 0)
food = Food(snake)
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
    
    # Столкновение со стенами или самой собой
    if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT or new_head in snake:
        running = False
    
    snake.insert(0, new_head)
    
    # Еда
    if new_head == (food.x, food.y):
        score += food.value  # Значение еды
        food.respawn(snake)  # Новая еда
        
        # Увеличение уровня каждые 4 очка
        if score % 4 == 0:
            level += 1
            speed += 2
    else:
        snake.pop()
    
    # Обновление таймера еды
    food.update(snake)
    
    # Отрисовка змейки
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))
    
    # Отрисовка еды 
    food_color = RED if food.value == 1 else BLUE if food.value == 2 else WHITE
    pygame.draw.rect(screen, food_color, (food.x, food.y, CELL_SIZE, CELL_SIZE))
    
    # Отображение счета и уровня
    font = pygame.font.Font(None, 30)
    score_text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    
    pygame.display.flip()
    clock.tick(speed)
    
pygame.quit()
