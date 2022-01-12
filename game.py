import pygame

from PipeCollection import PipeCollection
from bird import Bird
from constants import *
from ground import Base

bg_img = pygame.image.load('images/bg.png')
bg_img = pygame.transform.scale(bg_img, (DISPLAY_WIDTH, DISPLAY_HEIGHT))


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)

        self.score = 0
        self.running = True
        self.clock = pygame.time.Clock()
        self.ground = Base(FLOOR_HEIGHT)
        self.pipe_collection = PipeCollection()
        self.game_display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

    def run_game(self):
        bird = Bird(60, 270)
        # Use Game loop and tick it at FPS count (30)
        while self.running:
            self.clock.tick(FPS)
            self._handle_game_events(bird)
            self._update(bird)
            self._draw_window(bird)

            if bird.collide(self.pipe_collection):
                print('Collide')

    def _update(self, bird):
        bird.move()
        self.ground.move()
        self.pipe_collection.update()
        self._update_score(bird)

    def _update_score(self, bird):
        if len(self.pipe_collection.pipes) > 0:
            pipe = self.pipe_collection.pipes[0]
            if bird.x > pipe.x and not pipe.passed:
                pipe.passed = True
                self.score += 1
                print(self.score)

    def _draw_window(self, bird):
        self.game_display.blit(bg_img, (0, 0))

        self.pipe_collection.draw(self.game_display)
        self.ground.draw(self.game_display)
        bird.draw(self.game_display)

        font = pygame.font.SysFont('Bauhaus 93', 60)
        white = (255, 255, 255)
        x = int(DISPLAY_WIDTH / 2)
        y = 20
        draw_text(self.game_display, str(self.score), x, y, font, white)

        pygame.display.update()

    def _handle_game_events(self, bird):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.jump()


def draw_text(screen, text, x, y, font, white):
    img = font.render(text, True, white)
    screen.blit(img, (x - img.get_width() / 2, y))
