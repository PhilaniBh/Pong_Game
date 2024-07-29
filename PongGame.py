import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
BALL_SIZE = 20
PADDLE_WIDTH, PADDLE_HEIGHT = 100, 10
PADDLE_OFFSET = 50
BALL_SPEED_X, BALL_SPEED_Y = 4, 4
PADDLE_SPEED = 6
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Set up the clock
clock = pygame.time.Clock()

# Ball class
class Ball:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
        self.speed_x = BALL_SPEED_X
        self.speed_y = BALL_SPEED_Y

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.speed_y *= -1
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.speed_x *= -1

    def draw(self):
        pygame.draw.ellipse(screen, GREEN, self.rect)

# Paddle class
class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)

    def move(self, x_change):
        self.rect.x += x_change
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

    def draw(self):
        pygame.draw.rect(screen, WHITE, self.rect)

def display_game_over():
    font = pygame.font.Font(None, 74)
    text = font.render("Game Over", True, WHITE)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    pygame.display.flip()
    pygame.time.wait(3000)

# Game loop
def main():
    ball = Ball()
    paddle1 = Paddle(WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT - PADDLE_OFFSET)
    paddle2 = Paddle(WIDTH // 2 - PADDLE_WIDTH // 2, PADDLE_OFFSET - PADDLE_HEIGHT)

    running = True
    while running:
        # Keep the loop running at the right speed
        clock.tick(FPS)

        # Process input (events)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle1.move(-PADDLE_SPEED)
        if keys[pygame.K_RIGHT]:
            paddle1.move(PADDLE_SPEED)
        if keys[pygame.K_a]:
            paddle2.move(-PADDLE_SPEED)
        if keys[pygame.K_d]:
            paddle2.move(PADDLE_SPEED)

        # Move the ball
        ball.move()

        # Ball collision with paddles
        if ball.rect.colliderect(paddle1.rect) or ball.rect.colliderect(paddle2.rect):
            ball.speed_y *= -1

        # Check for game over
        if ball.rect.top > HEIGHT or ball.rect.bottom < 0:
            display_game_over()
            running = False

        # Draw / render
        screen.fill(BLACK)
        ball.draw()
        paddle1.draw()
        paddle2.draw()
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
