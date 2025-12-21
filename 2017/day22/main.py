import numpy as np


class Direction:
    def __init__(self):
        self.current = 0
        self.all_directions = ['up', 'right', 'down', 'left']

    def turn_right(self):
        self.current += 1
        if self.current == len(self.all_directions):
            self.current = 0
        return self.all_directions[self.current]

    def turn_left(self):
        self.current -= 1
        if self.current == -1:
            self.current = len(self.all_directions) - 1
        return self.all_directions[self.current]


def main():
    filename = 'input.txt'
    # filename = 'input_test.txt'
    puzzle_input: list[str] = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            puzzle_input.append(line.replace('\n', ''))

    # print(puzzle_input)  # 25x25 grid
    grid_size = len(puzzle_input)

    infected_nodes = []
    for i in range(grid_size):
        for j in range(grid_size):
            if puzzle_input[i][j] == '#':
                infected_nodes.append([i, j])

    start = grid_size // 2
    current_position = [start, start]

    n_bursts = 10000
    n_infections = 0
    direction = Direction()
    for _ in range(n_bursts):
        if current_position in infected_nodes:
            # print('direction before turn = ', current_dir)
            current_dir = direction.turn_right()
            # print('direction after turn = ', current_dir)
            infected_nodes.remove(current_position)
            current_position = move_forward(current_position, current_dir)
        else:
            current_dir = direction.turn_left()
            infected_nodes.append(current_position)
            n_infections += 1
            current_position = move_forward(current_position, current_dir)

        # print_table(current_position, infected_nodes)
        # print('-------------------------------------------')

    print('n_infections = ', n_infections)


def move_forward(current_position, direction):
    if direction == 'up':
        return [current_position[0] - 1, current_position[1]]
    elif direction == 'down':
        return [current_position[0] + 1, current_position[1]]
    elif direction == 'left':
        return [current_position[0], current_position[1] - 1]
    elif direction == 'right':
        return [current_position[0], current_position[1] + 1]


def print_table(current_position, infected_nodes):
    max_x, max_y = np.array(infected_nodes).max(axis=0)
    min_x, min_y = np.array(infected_nodes).min(axis=0)
    m = abs(min(min_x, min_y))
    size = max(max_x, max_y) + m
    size = 25
    grid = []
    for i in range(size):
        grid.append([])
        for j in range(size):
            grid[-1].append(' . ')

    for i, j in infected_nodes:
        grid[i+m][j+m] = ' # '

    i, j = current_position
    grid[i+m][j+m] = '[' + grid[i+m][j+m][1] + ']'

    for row in grid:
        print(row)

    # exit()


if __name__ == '__main__':
    main()
