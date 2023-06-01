import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Define the window size
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

# Define the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Set the font for the score
FONT = pygame.font.SysFont(None, 30)

# Define the directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Define the snake class
class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = GREEN
    
    def get_head_position(self):
        return self.positions[0]
    
    def turn(self, point):
        if self.length > 1 and (point[0]*-1, point[1]*-1) == self.direction:
            return
        else:
            self.direction = point
    
    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = ((cur[0] + (x*10)), (cur[1] + (y*10)))
        if new in self.positions:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()
    
    def reset(self):
        self.length = 1
        self.positions = [(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
    
    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (10, 10))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, BLACK, r, 1)

# Define the food class
class Food:
    def __init__(self):
        x = random.randint(0, (WINDOW_WIDTH - 10) / 10) * 10
        y = random.randint(0, (WINDOW_HEIGHT - 10) / 10) * 10
        self.position = (x, y)
        self.color = RED
    
    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (10, 10))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, BLACK, r, 1)

# Create the game window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Create the snake and food objects
snake = Snake()
food = Food()

# Define the game loop
clock = pygame.time.Clock()
score = 0

while True:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        snake.turn(LEFT)
    elif keys[pygame.K_RIGHT]:
        snake.turn(RIGHT)
    elif keys[pygame.K_UP]:
        snake.turn(UP)
    elif keys[pygame.K_DOWN]:
        snake.turn(DOWN)
    
    snake.move()
    if snake.get_head_position() == food.position:
        score += 1
        snake.length += 1
        food = Food()
        if score % 10 == 0:
            clock.tick(25)
    
    screen.fill(WHITE)
    snake.draw(screen)
    food.draw(screen)
    
    score_text = FONT.render("Score: {}".format(score), True, BLACK)
    screen.blit(score_text, (10, 10))
    
    pygame.display.update()
