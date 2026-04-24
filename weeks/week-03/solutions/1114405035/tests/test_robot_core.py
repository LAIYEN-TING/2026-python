import unittest
from robot_core import Robot, RobotWorld


class TestRobotCore(unittest.TestCase):
    def test_robot_turn_left(self):
        robot = Robot(0, 0, 'N')
        robot.turn_left()
        self.assertEqual(robot.direction, 'W')

        robot.turn_left()
        self.assertEqual(robot.direction, 'S')

    def test_robot_turn_right(self):
        robot = Robot(0, 0, 'N')
        robot.turn_right()
        self.assertEqual(robot.direction, 'E')

        robot.turn_right()
        self.assertEqual(robot.direction, 'S')

    def test_robot_move_forward_normal(self):
        world = RobotWorld(5, 5)
        world.add_robot(0, 0, 'N')
        world.execute_instruction('F')
        x, y, direction, lost = world.get_robot_state()
        self.assertEqual((x, y, direction, lost), (0, 1, 'N', False))

    def test_robot_lost_and_scent(self):
        world = RobotWorld(5, 5)
        world.add_robot(5, 5, 'N')  # 在邊界
        world.execute_instruction('F')  # 應該 LOST
        x, y, direction, lost = world.get_robot_state()
        self.assertEqual((x, y, direction, lost), (5, 5, 'N', True))
        self.assertIn((5, 5, 'N'), world.scents)

    def test_robot_ignore_instruction_with_scent(self):
        world = RobotWorld(5, 5)
        # 先讓一個機器人 LOST
        world.add_robot(5, 5, 'N')
        world.execute_instruction('F')
        self.assertIn((5, 5, 'N'), world.scents)

        # 新機器人在相同位置相同方向
        world.add_robot(5, 5, 'N')
        world.execute_instruction('F')  # 應該忽略
        x, y, direction, lost = world.get_robot_state()
        self.assertEqual((x, y, direction, lost), (5, 5, 'N', False))


if __name__ == '__main__':
    unittest.main()
