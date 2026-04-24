from typing import List, Tuple, Set


def parse_input_line(line: str) -> Tuple[int, int, str]:
    """解析輸入行，返回 x, y, direction"""
    parts = line.strip().split()
    if len(parts) != 3:
        raise ValueError("每行應包含 x y direction")
    x, y = int(parts[0]), int(parts[1])
    direction = parts[2]
    if direction not in 'NESW':
        raise ValueError("方向必須是 N/E/S/W")
    return x, y, direction


def parse_instructions(line: str) -> List[str]:
    """解析指令行，返回指令列表"""
    return [char for char in line.strip() if char in 'LRF']


def turn_left(direction: str) -> str:
    """左轉 90 度"""
    directions = 'NESW'
    idx = directions.index(direction)
    return directions[(idx - 1) % 4]


def turn_right(direction: str) -> str:
    """右轉 90 度"""
    directions = 'NESW'
    idx = directions.index(direction)
    return directions[(idx + 1) % 4]


def get_delta(direction: str) -> Tuple[int, int]:
    """獲取方向的位移"""
    deltas = {
        'N': (0, 1),
        'E': (1, 0),
        'S': (0, -1),
        'W': (-1, 0)
    }
    return deltas[direction]


def simulate_robot(grid_width: int, grid_height: int, start_x: int, start_y: int, start_dir: str, instructions: List[str], scents: Set[Tuple[int, int, str]]) -> Tuple[int, int, str, bool]:
    """模擬機器人移動，返回最終狀態"""
    x, y, direction = start_x, start_y, start_dir
    lost = False

    for instruction in instructions:
        if lost:
            break

        if instruction == 'L':
            direction = turn_left(direction)
        elif instruction == 'R':
            direction = turn_right(direction)
        elif instruction == 'F':
            dx, dy = get_delta(direction)
            new_x, new_y = x + dx, y + dy

            # 檢查是否會掉出地圖
            if new_x < 0 or new_x > grid_width or new_y < 0 or new_y > grid_height:
                # 檢查是否有 scent
                if (x, y, direction) in scents:
                    # 忽略指令
                    continue
                else:
                    # 標記 LOST 並留下 scent
                    lost = True
                    scents.add((x, y, direction))
            else:
                # 正常移動
                x, y = new_x, new_y

    return x, y, direction, lost


def process_robot_simulation(input_lines: List[str]) -> str:
    """處理整個模擬過程"""
    if not input_lines:
        return ""

    # 第一行：地圖大小
    grid_line = input_lines[0].strip().split()
    grid_width, grid_height = int(grid_line[0]), int(grid_line[1])

    scents: Set[Tuple[int, int, str]] = set()
    results = []

    i = 1
    while i < len(input_lines):
        # 機器人起始位置
        robot_line = input_lines[i].strip()
        if not robot_line:
            i += 1
            continue
        start_x, start_y, start_dir = parse_input_line(robot_line)

        # 指令
        i += 1
        if i >= len(input_lines):
            break
        instructions = parse_instructions(input_lines[i])

        # 模擬
        final_x, final_y, final_dir, lost = simulate_robot(grid_width, grid_height, start_x, start_y, start_dir, instructions, scents)

        # 輸出結果
        result = f"{final_x} {final_y} {final_dir}"
        if lost:
            result += " LOST"
        results.append(result)

        i += 1

    return '\n'.join(results)


def main() -> None:
    import sys
    input_lines = [line for line in sys.stdin if line.strip()]
    if input_lines:
        print(process_robot_simulation(input_lines))


if __name__ == '__main__':
    main()
