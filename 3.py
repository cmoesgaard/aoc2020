import math
import itertools


def get_input():
    with open('input/3', 'r') as f:
        return [line.strip() for line in f.readlines()]


def get_indices(step):
    return map(lambda x: x % 31, itertools.count(start=0, step=step))


def find_collision_in_list(input_tuple):
    input_list, indices = input_tuple

    def find_collision(line):
        string, index = line
        return string[index] == '#'

    zipped = zip(input_list, indices)
    filtered = filter(find_collision, zipped)
    return len(list(filtered))


def part_one():
    input_list = get_input()
    indices = get_indices(3)

    return find_collision_in_list((input_list, indices))


def part_two():
    input_list = get_input()

    inputs = [
        (input_list, get_indices(1)),
        (input_list, get_indices(3)),
        (input_list, get_indices(5)),
        (input_list, get_indices(7)),
        (input_list[::2], get_indices(1)),
    ]

    mapped = map(find_collision_in_list, inputs)
    return math.prod(mapped)


print(part_one())
print(part_two())
