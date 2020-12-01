from itertools import combinations

with open('input/1', 'r') as f:
    numbers = list(map(int, f.readlines()))


def find_values(number_list, num_of_combinations):
    for comb in combinations(number_list, num_of_combinations):
        if sum(comb) == 2020:
            return comb


def part_one():
    a, b = find_values(numbers, 2)
    return a * b


def part_two():
    a, b, c = find_values(numbers, 3)
    return a * b * c


print(part_one())
print(part_two())
