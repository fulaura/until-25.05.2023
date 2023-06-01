import pygame
import random
import sys

# Define some constants
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
GRID_SIZE = 20

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Define some directions
LEFT = (-1, 0)
RIGHT = (1, 0)
UP = (0, -1)
DOWN = (0, 1)

# Initialize Pygame
pygame.init()

# Set the window caption
pygame.display.set_caption("Snake Game")

# Create the game window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Load the font for the score display
FONT = pygame.font.Font(None, 24)

# Create the snake and food objects
class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [(0, 0)]
        self.direction = RIGHT
    
    def get_head_position(self):
        return self.positions[0]
    
    def turn(self, direction):
        if self.length > 1 and (direction[0] * -1, direction[1] * -1) == self.direction:
            return
        else:
            self.direction = direction
    
    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = ((cur[0] + (x * GRID_SIZE)) % WINDOW_WIDTH, (cur[1] + (y * GRID_SIZE)) % WINDOW_HEIGHT)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()
    
    def reset(self):
        self.length = 1
        self.positions = [(0, 0)]
        self.direction = RIGHT
    
    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(surface, GREEN, r)
            pygame.draw.rect(surface, WHITE, r, 1)

class Food:
    def __init__(self):
        self.position = (0, 0)
        self.randomize_position()
    
    def randomize_position(self):
        self.position = (random.randint(0, (WINDOW_WIDTH - GRID_SIZE) // GRID_SIZE) * GRID_SIZE,
                          random.randint(0, (WINDOW_HEIGHT - GRID_SIZE) // GRID_SIZE) * GRID_SIZE)
    
    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(surface, RED, r)
        pygame.draw.rect(surface, WHITE, r, 1)

snake = Snake()
food = Food()

# Create a clock object to manage the game's framerate
clock = pygame.time.Clock()

# Create a variable to keep track of the score
score = 0

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake.turn(LEFT)
