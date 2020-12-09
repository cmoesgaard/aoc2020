from functools import reduce

from more_itertools import split_at


def get_input():
    with open('input/6', 'r') as f:
        return [line.strip() for line in f.readlines()]


def process_input(input_str):
    group = split_at(input_str, lambda x: x == '')
    return group


def part_one():
    def count_answers(chunk):
        sets = map(set, chunk)
        union = reduce(lambda x, y: x.union(y), sets)
        return len(union)

    chunked_input = process_input(get_input())
    counts = map(count_answers, chunked_input)
    return sum(counts)


def part_two():
    def count_answers(chunk):
        sets = map(set, chunk)
        intersection = reduce(lambda x, y: x.intersection(y), sets)
        return len(intersection)

    chunked_input = process_input(get_input())
    counts = map(count_answers, chunked_input)
    return sum(counts)


print(part_one())
print(part_two())
