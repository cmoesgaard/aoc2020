import math
import itertools


def get_input():
    with open('input/3', 'r') as f:
        return [line.strip() for line in f.readlines()]


def get_indices(step):
    return map(lambda x: x % 31, itertools.count(start=0, step=step))


def find_collision_in_grid(input_tuple):
    def find_collision(line):
        string, index = line
        return string[index] == '#'

    grid, slope = input_tuple
    x_step, y_step = slope

    mapped_grid = grid[::y_step]
    indices = get_indices(x_step)

    zipped = zip(mapped_grid, indices)
    filtered = filter(find_collision, zipped)
    return len(list(filtered))


def part_one():
    grid = get_input()
    slope = (3, 1)
    return find_collision_in_grid((grid, slope))


def part_two():
    grid = get_input()
    slopes = [
        (1, 2),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]
    inputs = [(grid, slope) for slope in slopes]

    mapped = map(find_collision_in_grid, inputs)
    return math.prod(mapped)


print(part_one())
print(part_two())
