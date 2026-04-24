import pygame
import sys
from robot_core import RobotWorld
from typing import List, Tuple


class RobotGame:
    def __init__(self, grid_width: int = 5, grid_height: int = 5):
        pygame.init()

        self.grid_width = grid_width
        self.grid_height = grid_height
        self.cell_size = 60
        self.screen_width = (grid_width + 1) * self.cell_size
        self.screen_height = (grid_height + 1) * self.cell_size + 100  # 額外空間給按鈕

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Robot Lost Game")

        self.world = RobotWorld(grid_width, grid_height)
        self.font = pygame.font.Font(None, 24)
        self.clock = pygame.time.Clock()

        # 顏色
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GRAY = (200, 200, 200)
        self.RED = (255, 0, 0)
        self.BLUE = (0, 0, 255)
        self.GREEN = (0, 255, 0)

        # 按鈕區域
        self.button_y = (grid_height + 1) * self.cell_size
        self.button_height = 30
        self.button_width = 80

    def draw_grid(self) -> None:
        """繪製格子"""
        for x in range(self.grid_width + 1):
            pygame.draw.line(self.screen, self.BLACK,
                           (x * self.cell_size, 0),
                           (x * self.cell_size, self.grid_height * self.cell_size), 2)

        for y in range(self.grid_height + 1):
            pygame.draw.line(self.screen, self.BLACK,
                           (0, y * self.cell_size),
                           (self.grid_width * self.cell_size, y * self.cell_size), 2)

    def draw_robot(self) -> None:
        """繪製機器人"""
        if self.world.robot:
            x, y, direction, lost = self.world.get_robot_state()

            # 機器人位置
            center_x = x * self.cell_size + self.cell_size // 2
            center_y = (self.grid_height - y) * self.cell_size + self.cell_size // 2

            color = self.RED if lost else self.BLUE

            # 繪製機器人圓形
            pygame.draw.circle(self.screen, color, (center_x, center_y), self.cell_size // 3)

            # 繪製方向箭頭
            if not lost:
                arrow_length = self.cell_size // 4
                if direction == 'N':
                    end_y = center_y - arrow_length
                    pygame.draw.line(self.screen, self.BLACK, (center_x, center_y), (center_x, end_y), 3)
                    pygame.draw.polygon(self.screen, self.BLACK,
                                      [(center_x - 5, end_y + 5), (center_x, end_y), (center_x + 5, end_y + 5)])
                elif direction == 'S':
                    end_y = center_y + arrow_length
                    pygame.draw.line(self.screen, self.BLACK, (center_x, center_y), (center_x, end_y), 3)
                    pygame.draw.polygon(self.screen, self.BLACK,
                                      [(center_x - 5, end_y - 5), (center_x, end_y), (center_x + 5, end_y - 5)])
                elif direction == 'E':
                    end_x = center_x + arrow_length
                    pygame.draw.line(self.screen, self.BLACK, (center_x, center_y), (end_x, center_y), 3)
                    pygame.draw.polygon(self.screen, self.BLACK,
                                      [(end_x - 5, center_y - 5), (end_x, center_y), (end_x - 5, center_y + 5)])
                elif direction == 'W':
                    end_x = center_x - arrow_length
                    pygame.draw.line(self.screen, self.BLACK, (center_x, center_y), (end_x, center_y), 3)
                    pygame.draw.polygon(self.screen, self.BLACK,
                                      [(end_x + 5, center_y - 5), (end_x, center_y), (end_x + 5, center_y + 5)])

    def draw_scents(self) -> None:
        """繪製 scents"""
        for scent_x, scent_y, scent_dir in self.world.scents:
            center_x = scent_x * self.cell_size + self.cell_size // 2
            center_y = (self.grid_height - scent_y) * self.cell_size + self.cell_size // 2

            # 繪製 scent 標記
            pygame.draw.circle(self.screen, self.GREEN, (center_x, center_y), 5)

    def draw_buttons(self) -> None:
        """繪製按鈕"""
        buttons = [
            ("Reset Robot", 10),
            ("Clear Scents", 100),
            ("Replay", 190)
        ]

        for text, x in buttons:
            rect = pygame.Rect(x, self.button_y, self.button_width, self.button_height)
            pygame.draw.rect(self.screen, self.GRAY, rect)
            pygame.draw.rect(self.screen, self.BLACK, rect, 2)

            text_surf = self.font.render(text, True, self.BLACK)
            text_rect = text_surf.get_rect(center=rect.center)
            self.screen.blit(text_surf, text_rect)

    def draw_status(self) -> None:
        """繪製狀態資訊"""
        if self.world.robot:
            x, y, direction, lost = self.world.get_robot_state()
            status = f"Position: ({x}, {y}) Direction: {direction}"
            if lost:
                status += " LOST"
        else:
            status = "No robot"

        text_surf = self.font.render(status, True, self.BLACK)
        self.screen.blit(text_surf, (10, self.button_y + 40))

        # 顯示指令歷史
        history_text = "Instructions: " + ''.join(self.world.instruction_history[-10:])  # 顯示最後10個
        history_surf = self.font.render(history_text, True, self.BLACK)
        self.screen.blit(history_surf, (10, self.button_y + 60))

    def handle_button_click(self, pos: Tuple[int, int]) -> None:
        """處理按鈕點擊"""
        x, y = pos
        if y < self.button_y or y > self.button_y + self.button_height:
            return

        if 10 <= x <= 10 + self.button_width:
            self.world.reset_robot()
        elif 100 <= x <= 100 + self.button_width:
            self.world.clear_scents()
        elif 190 <= x <= 190 + self.button_width:
            # Replay 功能（簡化版：重新執行指令）
            if self.world.robot and self.world.instruction_history:
                self.world.reset_robot()
                # 這裡可以實作重播動畫，但先簡化為重新執行

    def run(self) -> None:
        """主遊戲迴圈"""
        running = True

        # 新增測試機器人
        self.world.add_robot(0, 0, 'N')

        while running:
            self.screen.fill(self.WHITE)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_l:
                        self.world.execute_instruction('L')
                    elif event.key == pygame.K_r:
                        self.world.execute_instruction('R')
                    elif event.key == pygame.K_f:
                        self.world.execute_instruction('F')
                    elif event.key == pygame.K_SPACE:
                        self.world.reset_robot()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_button_click(event.pos)

            self.draw_grid()
            self.draw_scents()
            self.draw_robot()
            self.draw_buttons()
            self.draw_status()

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    game = RobotGame()
    game.run()
