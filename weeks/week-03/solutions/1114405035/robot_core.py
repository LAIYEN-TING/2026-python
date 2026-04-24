from typing import List, Tuple, Set


class Robot:
    def __init__(self, x: int, y: int, direction: str):
        self.x = x
        self.y = y
        self.direction = direction
        self.lost = False

    def turn_left(self) -> None:
        """左轉 90 度"""
        directions = 'NESW'
        idx = directions.index(self.direction)
        self.direction = directions[(idx - 1) % 4]

    def turn_right(self) -> None:
        """右轉 90 度"""
        directions = 'NESW'
        idx = directions.index(self.direction)
        self.direction = directions[(idx + 1) % 4]

    def get_next_position(self) -> Tuple[int, int]:
        """獲取前進後的位置"""
        deltas = {
            'N': (0, 1),
            'E': (1, 0),
            'S': (0, -1),
            'W': (-1, 0)
        }
        dx, dy = deltas[self.direction]
        return self.x + dx, self.y + dy

    def move_forward(self, grid_width: int, grid_height: int, scents: Set[Tuple[int, int, str]]) -> bool:
        """嘗試前進，如果會掉出地圖則標記 LOST"""
        next_x, next_y = self.get_next_position()

        if next_x < 0 or next_x > grid_width or next_y < 0 or next_y > grid_height:
            # 檢查是否有 scent
            if (self.x, self.y, self.direction) in scents:
                return False  # 忽略指令
            else:
                # 標記 LOST 並留下 scent
                self.lost = True
                scents.add((self.x, self.y, self.direction))
                return True
        else:
            # 正常移動
            self.x, self.y = next_x, next_y
            return True


class RobotWorld:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.scents: Set[Tuple[int, int, str]] = set()
        self.robot = None
        self.instruction_history: List[str] = []

    def add_robot(self, x: int, y: int, direction: str) -> None:
        """新增機器人"""
        self.robot = Robot(x, y, direction)
        self.instruction_history = []

    def execute_instruction(self, instruction: str) -> bool:
        """執行單一指令，返回是否成功執行"""
        if not self.robot or self.robot.lost:
            return False

        if instruction == 'L':
            self.robot.turn_left()
        elif instruction == 'R':
            self.robot.turn_right()
        elif instruction == 'F':
            if not self.robot.move_forward(self.width, self.height, self.scents):
                return False  # 指令被忽略
        else:
            return False  # 無效指令

        self.instruction_history.append(instruction)
        return True

    def execute_instructions(self, instructions: str) -> None:
        """執行一串指令"""
        for char in instructions.upper():
            if char in 'LRF':
                self.execute_instruction(char)

    def reset_robot(self) -> None:
        """重置機器人，保留 scents"""
        self.robot = None
        self.instruction_history = []

    def clear_scents(self) -> None:
        """清除所有 scents"""
        self.scents.clear()

    def get_robot_state(self) -> Tuple[int, int, str, bool]:
        """獲取機器人狀態"""
        if self.robot:
            return self.robot.x, self.robot.y, self.robot.direction, self.robot.lost
        return 0, 0, 'N', False

    def replay_instructions(self) -> List[Tuple[int, int, str]]:
        """重播指令，返回每個步驟的狀態"""
        if not self.robot:
            return []

        # 儲存初始狀態
        initial_x, initial_y, initial_dir = self.robot.x, self.robot.y, self.robot.direction
        initial_lost = self.robot.lost

        states = [(initial_x, initial_y, initial_dir)]

        # 重新執行指令
        for instruction in self.instruction_history:
            self.execute_instruction(instruction)
            states.append((self.robot.x, self.robot.y, self.robot.direction))

        # 恢復狀態
        self.robot.x, self.robot.y, self.robot.direction, self.robot.lost = initial_x, initial_y, initial_dir, initial_lost

        return states
