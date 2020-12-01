import math
from itertools import combinations

with open('input/1', 'r') as f:
    numbers = list(map(int, f.readlines()))


def find_values(number_list, num_of_combinations):
    combis = combinations(number_list, num_of_combinations)
    filtered = filter(lambda x: sum(x) == 2020, combis)
    prods = map(math.prod, filtered)
    return prods


def part_one():
    return find_values(numbers, 2)


def part_two():
    return find_values(numbers, 3)


print(list(part_one()))
print(list(part_two()))
