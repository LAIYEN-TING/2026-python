import sys
from robot_core import RobotWorld
from typing import List, Tuple


class TextBasedRobotGame:
    def __init__(self, grid_width: int = 5, grid_height: int = 5):
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.world = RobotWorld(grid_width, grid_height)
        self.world.add_robot(0, 0, 'N')

    def print_grid(self) -> None:
        """以文字方式印出格子"""
        print(f"\n地圖 ({self.grid_width}x{self.grid_height}):")
        print("=" * (self.grid_width * 2 + 1))

        for y in range(self.grid_height - 1, -1, -1):  # Y 軸從上到下
            row = "|"
            for x in range(self.grid_width + 1):
                # 檢查是否有機器人
                if self.world.robot and self.world.robot.x == x and self.world.robot.y == y:
                    if self.world.robot.lost:
                        row += "X|"  # LOST 機器人
                    else:
                        row += f"{self.world.robot.direction}|"  # 方向
                # 檢查是否有 scent
                elif (x, y, 'N') in self.world.scents or (x, y, 'E') in self.world.scents or \
                     (x, y, 'S') in self.world.scents or (x, y, 'W') in self.world.scents:
                    row += "S|"  # Scent
                else:
                    row += " |"  # 空位
            print(row)
            print("-" * (self.grid_width * 2 + 1))

    def print_status(self) -> None:
        """印出狀態"""
        if self.world.robot:
            x, y, direction, lost = self.world.get_robot_state()
            status = f"機器人位置: ({x}, {y}) 方向: {direction}"
            if lost:
                status += " [LOST]"
            print(status)
        else:
            print("沒有機器人")

        print(f"指令歷史: {''.join(self.world.instruction_history)}")
        print(f"Scents 數量: {len(self.world.scents)}")

    def run(self) -> None:
        """主遊戲迴圈"""
        print("=== 機器人遊戲 (文字版) ===")
        print("指令: L(左轉) R(右轉) F(前進) Q(離開) C(清除scents) N(新機器人)")

        while True:
            self.print_grid()
            self.print_status()

            try:
                command = input("\n輸入指令: ").strip().upper()
            except (EOFError, KeyboardInterrupt):
                break

            if command == 'Q':
                break
            elif command == 'C':
                self.world.clear_scents()
                print("已清除所有 scents")
            elif command == 'N':
                self.world.reset_robot()
                self.world.add_robot(0, 0, 'N')
                print("已新增機器人")
            elif command in 'LRF':
                success = self.world.execute_instruction(command)
                if not success:
                    print("指令被忽略 (scent 保護)")
            else:
                print("無效指令，請輸入 L/R/F/Q/C/N")

        print("遊戲結束")


if __name__ == '__main__':
    game = TextBasedRobotGame()
    game.run()
