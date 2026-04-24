class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.scents = set()

    def is_out_of_bounds(self, x, y):
        return x < 0 or x > self.width or y < 0 or y > self.height

    def add_scent(self, x, y, direction):
        self.scents.add((x, y, direction))

    def has_scent(self, x, y, direction):
        return (x, y, direction) in self.scents

class Robot:
    DIRECTIONS = ['N', 'E', 'S', 'W']
    MOVE_MAP = {
        'N': (0, 1),
        'E': (1, 0),
        'S': (0, -1),
        'W': (-1, 0)
    }

    def __init__(self, x, y, direction, world):
        self.x = x
        self.y = y
        self.direction = direction
        self.world = world
        self.lost = False
        self.history = [(x, y, direction)]

    def turn_left(self):
        if self.lost: return
        idx = self.DIRECTIONS.index(self.direction)
        self.direction = self.DIRECTIONS[(idx - 1) % 4]
        self.history.append((self.x, self.y, self.direction))

    def turn_right(self):
        if self.lost: return
        idx = self.DIRECTIONS.index(self.direction)
        self.direction = self.DIRECTIONS[(idx + 1) % 4]
        self.history.append((self.x, self.y, self.direction))

    def move_forward(self):
        if self.lost: return
        
        dx, dy = self.MOVE_MAP[self.direction]
        new_x, new_y = self.x + dx, self.y + dy

        if self.world.is_out_of_bounds(new_x, new_y):
            if self.world.has_scent(self.x, self.y, self.direction):
                # Ignore the dangerous instruction
                return
            else:
                # Robot is lost
                self.lost = True
                self.world.add_scent(self.x, self.y, self.direction)
        else:
            self.x, self.y = new_x, new_y
            self.history.append((self.x, self.y, self.direction))

    def execute_commands(self, commands):
        for cmd in commands:
            if self.lost: break
            if cmd == 'L':
                self.turn_left()
            elif cmd == 'R':
                self.turn_right()
            elif cmd == 'F':
                self.move_forward()
            # Ignore unknown commands
