import pygame
import sys
from robot_core import World, Robot

# Constants
CELL_SIZE = 60
MARGIN = 50
WIDTH_CELLS = 5
HEIGHT_CELLS = 3
SCREEN_WIDTH = (WIDTH_CELLS + 1) * CELL_SIZE + 2 * MARGIN
SCREEN_HEIGHT = (HEIGHT_CELLS + 1) * CELL_SIZE + 2 * MARGIN
FPS = 30

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)

class RobotGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Robot Lost - Week 03")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 20)
        self.big_font = pygame.font.SysFont("Arial", 24, bold=True)
        
        self.world = World(WIDTH_CELLS, HEIGHT_CELLS)
        self.spawn_robot()
        self.message = "Use L, R, F to move. N: New, C: Clear Scents"

    def spawn_robot(self, x=1, y=1, d='N'):
        self.robot = Robot(x, y, d, self.world)

    def grid_to_screen(self, x, y):
        # Origin (0,0) is bottom-left in logical world, but top-left in pygame
        screen_x = MARGIN + x * CELL_SIZE
        screen_y = MARGIN + (self.world.height - y) * CELL_SIZE
        return screen_x, screen_y

    def draw_grid(self):
        for x in range(self.world.width + 1):
            for y in range(self.world.height + 1):
                px, py = self.grid_to_screen(x, y)
                pygame.draw.rect(self.screen, GRAY, (px, py, CELL_SIZE, CELL_SIZE), 1)
                label = self.font.render(f"({x},{y})", True, GRAY)
                self.screen.blit(label, (px + 5, py + 5))

    def draw_scents(self):
        for sx, sy, sd in self.world.scents:
            px, py = self.grid_to_screen(sx, sy)
            pygame.draw.circle(self.screen, ORANGE, (px + CELL_SIZE // 2, py + CELL_SIZE // 2), 10)
            s_label = self.font.render(sd, True, WHITE)
            self.screen.blit(s_label, (px + CELL_SIZE // 2 - 5, py + CELL_SIZE // 2 - 10))

    def draw_robot(self):
        px, py = self.grid_to_screen(self.robot.x, self.robot.y)
        color = RED if self.robot.lost else GREEN
        center = (px + CELL_SIZE // 2, py + CELL_SIZE // 2)
        
        # Draw robot body
        pygame.draw.circle(self.screen, color, center, 20)
        
        # Draw direction arrow
        d = self.robot.direction
        offset = 15
        if d == 'N': end = (center[0], center[1] - offset)
        elif d == 'E': end = (center[0] + offset, center[1])
        elif d == 'S': end = (center[1], center[1] + offset) # wait, center is tuple
        elif d == 'S': end = (center[0], center[1] + offset)
        elif d == 'W': end = (center[0] - offset, center[1])
        
        pygame.draw.line(self.screen, WHITE, center, end, 3)

    def draw_info(self):
        status = f"Pos: ({self.robot.x}, {self.robot.y}) Dir: {self.robot.direction}"
        if self.robot.lost: status += " - LOST!"
        
        img = self.big_font.render(status, True, BLACK)
        self.screen.blit(img, (MARGIN, 10))
        
        msg_img = self.font.render(self.message, True, BLUE)
        self.screen.blit(msg_img, (MARGIN, SCREEN_HEIGHT - 35))

    def run(self):
        while True:
            self.screen.fill(WHITE)
            self.draw_grid()
            self.draw_scents()
            self.draw_robot()
            self.draw_info()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_l:
                        self.robot.turn_left()
                    elif event.key == pygame.K_r:
                        self.robot.turn_right()
                    elif event.key == pygame.K_f:
                        self.robot.move_forward()
                    elif event.key == pygame.K_n:
                        self.spawn_robot()
                    elif event.key == pygame.K_c:
                        self.world.scents.clear()
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            pygame.display.flip()
            self.clock.tick(FPS)

if __name__ == "__main__":
    game = RobotGame()
    game.run()
