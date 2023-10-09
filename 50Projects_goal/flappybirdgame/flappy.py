import pygame
import random

# Game dimensions
WIDTH = 288
HEIGHT = 512

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Flappy Bird")
    clock = pygame.time.Clock()
    
    # Load images
    background = pygame.image.load("background.png").convert()
    bird_img = pygame.image.load("bird.png").convert_alpha()
    pipe_img = pygame.image.load("pipe.png").convert_alpha()
    
    # Bird properties
    bird_x = 50
    bird_y = int(HEIGHT / 2)
    bird_y_change = 0
    
    # Pipe properties
    pipe_x = WIDTH
    pipe_height = [200, 250, 300, 350]
    pipe_gap = 100
    pipe_width = 52
    pipe_list = []
    
    # Score
    score = 0
    font = pygame.font.Font(None, 36)
    
    # Game over flag
    game_over = False
    
    def draw_bird(x, y):
        screen.blit(bird_img, (x, y))
    
    def draw_pipes(x, height):
        screen.blit(pipe_img, (x, 0 - height))
        screen.blit(pipe_img, (x, pipe_gap + height))
    
    def display_score(score):
        text = font.render("Score: " + str(score), True, WHITE)
        screen.blit(text, (10, 10))
    
    def is_collision(x, y, pipes):
        if y < 0 or y + bird_img.get_height() > HEIGHT:
            return True
        for pipe in pipes:
            if x + bird_img.get_width() > pipe["x"] and x < pipe["x"] + pipe_width:
                if y < pipe["height"] or y + bird_img.get_height() > pipe["height"] + pipe_gap:
                    return True
        return False
    
    def game_over_screen():
        screen.fill(BLACK)
        text = font.render("Game Over", True, WHITE)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
        pygame.display.flip()
        pygame.time.wait(2000)
    
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird_y_change = -5
        
        bird_y += bird_y_change
        
        screen.blit(background, (0, 0))
        
        if bird_y > HEIGHT - bird_img.get_height():
            bird_y = HEIGHT - bird_img.get_height()
        
        if bird_y < 0:
            bird_y = 0
        
        if pipe_x < -pipe_width:
            pipe_x = WIDTH
            pipe_height = random.choice(pipe_height)
            score += 1
        
        if is_collision(bird_x, bird_y, pipe_list):
            game_over = True
        
        draw_bird(bird_x, bird_y)
        
        for pipe in pipe_list:
            pipe["x"] -= 5
            draw_pipes(pipe["x"], pipe["height"])
        
        display_score(score)
        
        if pipe_x < WIDTH - pipe_width - 200:
            new_pipe = {"x": WIDTH, "height": pipe_height}
            pipe
