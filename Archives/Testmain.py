import pygame
import sys
import random
from bird import FlappyBird 
from pipe import Pipe

class Game:
    # Initialize Pygame
    def __init__(self, screen_width, screen_height):
        pygame.init()

        # Set up the screen
        self.screen_width  = 1920
        self.screen_height = 1080
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Flappy Bird")

        # Set up colors
        self.white = (255, 255, 255)
        self.GRAY = (128, 128, 128)


        # Set up clock
        self.clock = pygame.time.Clock()

        # Create sprite groups
        self.birds = pygame.sprite.Group()
        self.pipes = pygame.sprite.Group()

        # Set up the bird
        self.bird = FlappyBird(screen_width // 4, screen_height // 2, "plane.png")  # Initial position
        self.birds.add(self.bird)

        # Set up pipes
        self.pipe_gap = 300
        self.pipe_spawn_frequency = 80  # in frames
        self.pipe_spawn_timer = 0

        # Game loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.bird.flap()

            # Update bird
            self.bird.update(screen_height)
            
            # Update the pipes
            speed = 5  # Set a constant speed
            self.pipes.update(speed)  
            
            # Spawn pipes
            self.pipe_spawn_timer += 1
            if self.pipe_spawn_timer == self.pipe_spawn_frequency:
                pipe_height = random.randint(200, 600)
                new_pipe = Pipe(self.screen_width, pipe_height, self.pipe_gap)
                self.pipes.add(new_pipe)
                self.pipe_spawn_timer = 0


            # Remove offscreen pipes
            for pipe in self.pipes:
                if pipe.offscreen():
                    self.pipes.remove(pipe)

            # Check for collisions with pipes
            for pipe in self.pipes:
                if self.bird.rect.x < pipe.x + pipe.width and self.bird.rect.x + self.bird.rect.width > pipe.x:
                    if self.bird.rect.y < pipe.height or self.bird.rect.y + self.bird.rect.height > pipe.height + pipe.gap:
                        print("Ouch! You hit a pipe!")
                        pygame.quit()
                        sys.exit() 

            # Draw everything
            self.screen.fill(self.white)

            # Draw pipes first
            for pipe in self.pipes:
                pipe.draw(self.screen, self.GRAY)  # Pass the pipe color

            # Draw bird last
            self.bird.draw(self.screen)

            pygame.display.flip()


            # Cap the frame rate
            self.clock.tick(60)  # Adjust as needed
if __name__ == "__main__":
    game =  Game(1920, 1080)
    game.run()