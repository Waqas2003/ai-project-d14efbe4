Here is the code for a Snake Game in Python, separated into multiple files:

# file: game/__init__.py
```
# empty file
```

# file: game/config.py
```
WIDTH, HEIGHT = 800, 600
BLOCK_SIZE = 20
SPEED = 10
```

# file: game/models.py
```
from enum import Enum

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class Snake:
    def __init__(self):
        self.body = [(200, 200), (220, 200), (240, 200)]
        self.direction = Direction.RIGHT

    def move(self):
        head = self.body[0]
        if self.direction == Direction.UP:
            new_head = (head[0], head[1] - 20)
        elif self.direction == Direction.DOWN:
            new_head = (head[0], head[1] + 20)
        elif self.direction == Direction.LEFT:
            new_head = (head[0] - 20, head[1])
        elif self.direction == Direction.RIGHT:
            new_head = (head[0] + 20, head[1])
        self.body.insert(0, new_head)

    def eat(self, food):
        if self.body[0] == food:
            return True
        else:
            self.body.pop()
            return False

class Food:
    def __init__(self):
        self.position = (400, 300)

    def generate(self):
        self.position = (random.randint(0, WIDTH - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE,
                         random.randint(0, HEIGHT - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE)
```

# file: game/views.py
```
import pygame
from .models import Snake, Food, Direction

class GameView:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()
        self.food.generate()
        self.score = 0

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.snake.direction != Direction.DOWN:
                    self.snake.direction = Direction.UP
                elif event.key == pygame.K_DOWN and self.snake.direction != Direction.UP:
                    self.snake.direction = Direction.DOWN
                elif event.key == pygame.K_LEFT and self.snake.direction != Direction.RIGHT:
                    self.snake.direction = Direction.LEFT
                elif event.key == pygame.K_RIGHT and self.snake.direction != Direction.LEFT:
                    self.snake.direction = Direction.RIGHT

    def update(self):
        self.snake.move()
        if self.snake.eat(self.food.position):
            self.score += 1
            self.food.generate()
        else:
            self.snake.body.pop()

    def render(self, screen):
        screen.fill((0, 0, 0))
        for x, y in self.snake.body:
            pygame.draw.rect(screen, (0, 255, 0), (x, y, 20, 20))
        pygame.draw.rect(screen, (255, 0, 0), (self.food.position[0], self.food.position[1], 20, 20))
        font = pygame.font.Font(None, 36)
        text = font.render(f'Score: {self.score}', True, (255, 255, 255))
        screen.blit(text, (10, 10))
        pygame.display.flip()
```

# file: game/main.py
```
import pygame
from .views import GameView

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Snake Game')
    clock = pygame.time.Clock()
    game_view = GameView()
    running = True
    while running:
        game_view.handle_events()
        game_view.update()
        game_view.render(screen)
        clock.tick(10)
    pygame.quit()

if __name__ == '__main__':
    main()
```

# file: requirements.txt
```
pygame
```

# file: README.md
```
Snake Game in Python
=====================

A simple implementation of the classic Snake game using Python and Pygame.

To run the game, simply execute `python game/main.py` in your terminal.

Use the arrow keys to control the snake, and try to eat as much food as possible!

Note: This game uses a fixed window size of 800x600, and the game speed is set to 10 FPS. You can adjust these settings in the `game/config.py` file.
```