import pygame

from pipe_collection import PipeCollection
from bird import Bird
from constants import *
from ground import Base

bg_img = pygame.image.load(BACKGROUND_FILENAME)
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
        self.bird = Bird(BIRD_STARTER_X, BIRD_STARTER_Y)

    def run_game(self):
        # Use Game loop and tick it at FPS count (30)
        while self.running:
            self.clock.tick(FPS)
            self._handle_game_events(self.bird)
            self._update(self.bird)
            self._draw_window(self.bird)

            if self.bird.collide(self.pipe_collection):
                self.reset()

    def reset(self):
        self.pipe_collection = PipeCollection()
        self.bird = Bird(BIRD_STARTER_X, BIRD_STARTER_Y)
        self.score = 0

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

        draw_text(self.game_display, str(self.score), X_SCORE_POS, Y_SCORE_POS, SCORE_FONT, SCORE_SIZE, WHITE)

        pygame.display.update()

    def _handle_game_events(self, bird):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.jump()


def draw_text(screen, text, x, y, font, size, white):
    font = pygame.font.SysFont(font, size)
    img = font.render(text, True, white)
    screen.blit(img, (x - img.get_width() / 2, y))
