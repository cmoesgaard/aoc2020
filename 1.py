import math
from itertools import combinations


def get_numbers():
    with open('input/1', 'r') as f:
        return map(int, f.readlines())


def find_products(numbers, num_of_combinations):
    combis = combinations(numbers, num_of_combinations)
    filtered = filter(lambda x: sum(x) == 2020, combis)
    prods = map(math.prod, filtered)
    return prods


def part_one():
    numbers = get_numbers()
    return find_products(numbers, 2)


def part_two():
    numbers = get_numbers()
    return find_products(numbers, 3)


print(list(part_one()))
print(list(part_two()))
