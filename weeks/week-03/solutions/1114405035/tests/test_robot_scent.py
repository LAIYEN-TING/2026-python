import unittest
from robot_core import RobotWorld


class TestRobotScent(unittest.TestCase):
    def test_scent_prevents_loss(self):
        world = RobotWorld(5, 5)

        # 第一個機器人 LOST 並留下 scent
        world.add_robot(5, 5, 'N')
        world.execute_instruction('F')
        self.assertTrue(world.robot.lost)
        self.assertIn((5, 5, 'N'), world.scents)

        # 第二個機器人在相同位置相同方向
        world.add_robot(5, 5, 'N')
        initial_x, initial_y, initial_dir, initial_lost = world.get_robot_state()

        # 執行 F 應該被忽略
        world.execute_instruction('F')
        final_x, final_y, final_dir, final_lost = world.get_robot_state()

        self.assertEqual((initial_x, initial_y, initial_dir, initial_lost),
                        (final_x, final_y, final_dir, final_lost))
        self.assertFalse(final_lost)

    def test_scent_different_direction_no_effect(self):
        world = RobotWorld(5, 5)

        # LOST 在 'N' 方向
        world.add_robot(5, 5, 'N')
        world.execute_instruction('F')
        self.assertIn((5, 5, 'N'), world.scents)

        # 新機器人在相同位置但不同方向
        world.add_robot(5, 5, 'E')
        world.execute_instruction('F')  # 應該 LOST，因為沒有 'E' 方向的 scent
        self.assertTrue(world.robot.lost)
        self.assertIn((5, 5, 'E'), world.scents)

    def test_clear_scents(self):
        world = RobotWorld(5, 5)
        world.add_robot(5, 5, 'N')
        world.execute_instruction('F')
        self.assertTrue(len(world.scents) > 0)

        world.clear_scents()
        self.assertEqual(len(world.scents), 0)


if __name__ == '__main__':
    unittest.main()
