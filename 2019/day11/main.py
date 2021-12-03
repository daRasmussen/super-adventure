from intcode import Intcode

class RobotGrid:
    grid = {}
    robot_pos = tuple([0, 0])
    dirs = [[0, -1], [1, 0], [0, 1], [-1, 0]] # up, right, down left
    dir_index = 0
    def __init__(self, grid):
        self.grid = grid
    def get_panel_color(self):
        return int(self.grid.get(self.robot_pos, 0))
    def paint_panel(self, color):
        newly_painted = self.grid.get(self.robot_pos) is None
        self.grid[self.robot_pos] = color
        return newly_painted
    def move_robot(self, next_dir):
        if next_dir == 1: # turn right 90 degrees
            self.dir_index += 1
        elif next_dir == 0: # turn left 90 degrees
            self.dir_index -= 1
        dir_vector = self.dirs[self.dir_index % len(self.dirs)]
        self.robot_pos = tuple([self.robot_pos[0] + dir_vector[0], self.robot_pos[1] + dir_vector[1]])
def _get_program(file):
    with open(file) as f:
        return list(map(int, f.read().split(",")))
def _print_hull(hull):
    hull_str = []
    for row in hull:
        hull_str.append("".join(row))
    return "\n".join(hull_str)
# part 1
grid = {}
data = _get_program("data.txt")
vm = Intcode(data)
robot_grid = RobotGrid(grid)
painted_count = 0
while True:
    curr_color = robot_grid.get_panel_color()
    vm.set_input(curr_color)
    color = vm.run()
    if color is None:
        break
    painted_count += 1 if robot_grid.paint_panel(color) else 0
    vm.set_input(curr_color)
    robot_grid.move_robot(vm.run())
print(painted_count)
