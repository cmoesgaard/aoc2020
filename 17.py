from functools import partial
from itertools import product

from more_itertools import flatten, iterate, nth


def get_input():
    with open("input/17", "r") as f:
        return [line.strip() for line in f.readlines()]


def create_coordinates(input_list, dimensions: int):
    extra_dimensions = dimensions - 2
    extra = set()
    if extra_dimensions:
        extra = tuple([0] * extra_dimensions)

    coord_set = set()
    for x, line in enumerate(input_list):
        for y, char in enumerate(line):
            if char == "#":
                coord_set.add((int(x), int(y)) + extra)
    return coord_set


def generate_neighbor_coordinates(coordinate):
    def adjacent(i):
        return int(i) - 1, int(i), int(i) + 1

    return set(product(*(map(adjacent, coordinate)))) - {coordinate}


def filter_survivor(coordinate, grid):
    neighbors = generate_neighbor_coordinates(coordinate)
    intersection = set(grid).intersection(neighbors)
    if coordinate in grid:
        return 2 <= len(intersection) <= 3
    else:
        return len(intersection) == 3


def generate_cycle(grid: set):
    neighbors = set(flatten(map(generate_neighbor_coordinates, grid)))
    all_coordinates = grid.union(neighbors)
    filter_fn = partial(filter_survivor, grid=grid)
    return set(filter(filter_fn, all_coordinates))


def part_one():
    input_lines = get_input()
    coordinates = create_coordinates(input_lines, 3)
    cycles = iterate(generate_cycle, coordinates)
    return len(nth(cycles, 6))


def part_two():
    input_lines = get_input()
    coordinates = create_coordinates(input_lines, 4)
    cycles = iterate(generate_cycle, coordinates)
    return len(nth(cycles, 6))


print(part_one())
print(part_two())
