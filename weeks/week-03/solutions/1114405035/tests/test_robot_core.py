import unittest
from robot_core import Robot, World

class TestRobotCore(unittest.TestCase):
    def setUp(self):
        self.world = World(5, 3)

    def test_initial_position(self):
        robot = Robot(1, 1, 'E', self.world)
        self.assertEqual((robot.x, robot.y, robot.direction), (1, 1, 'E'))

    def test_turn_left(self):
        robot = Robot(1, 1, 'N', self.world)
        robot.turn_left()
        self.assertEqual(robot.direction, 'W')
        robot.turn_left()
        self.assertEqual(robot.direction, 'S')

    def test_turn_right(self):
        robot = Robot(1, 1, 'N', self.world)
        robot.turn_right()
        self.assertEqual(robot.direction, 'E')
        robot.turn_right()
        self.assertEqual(robot.direction, 'S')

    def test_move_forward(self):
        robot = Robot(1, 1, 'N', self.world)
        robot.move_forward()
        self.assertEqual((robot.x, robot.y), (1, 2))

    def test_move_out_of_bounds(self):
        robot = Robot(1, 1, 'N', self.world)
        # Move to top edge
        robot.move_forward() # (1,2)
        robot.move_forward() # (1,3)
        robot.move_forward() # LOST at (1,3)
        self.assertTrue(robot.lost)
        self.assertEqual((robot.x, robot.y), (1, 3))
        self.assertIn((1, 3, 'N'), self.world.scents)

    def test_scent_ignores_danger(self):
        self.world.add_scent(1, 3, 'N')
        robot = Robot(1, 3, 'N', self.world)
        robot.move_forward()
        # Should NOT move and NOT be lost
        self.assertEqual((robot.x, robot.y), (1, 3))
        self.assertFalse(robot.lost)

    def test_complex_commands(self):
        # UVA Sample: 1 1 E RFRFRFRF
        robot = Robot(1, 1, 'E', self.world)
        robot.execute_commands("RFRFRFRF")
        self.assertEqual((robot.x, robot.y, robot.direction), (1, 1, 'E'))
        self.assertFalse(robot.lost)

    def test_lost_robot_stops_executing(self):
        robot = Robot(1, 1, 'N', self.world)
        # Force lost
        robot.execute_commands("FFFFF")
        self.assertTrue(robot.lost)
        last_x, last_y = robot.x, robot.y
        robot.turn_left() # Should be ignored
        self.assertEqual(robot.x, last_x)
        self.assertEqual(robot.y, last_y)

    def test_different_scent_directions(self):
        self.world.add_scent(1, 3, 'N')
        robot = Robot(1, 3, 'E', self.world)
        # Robot is at (1,3) facing E. Moving F is safe.
        robot.move_forward()
        self.assertEqual((robot.x, robot.y), (2, 3))

    def test_invalid_command(self):
        robot = Robot(1, 1, 'N', self.world)
        robot.execute_commands("FXF")
        self.assertEqual((robot.x, robot.y), (1, 3))

if __name__ == '__main__':
    unittest.main()
