def get_input():
    with open('input/2', 'r') as f:
        return [line.strip() for line in f.readlines()]


def filter_passwords(input_list, filter_fn_generator):
    tuples = [line.split(': ') for line in input_list]
    mapped = [filter_fn_generator(policy)(password) for policy, password in tuples]
    return mapped.count(True)


def part_one():
    puzzle_input = get_input()

    def generate_filter_fn(policy):
        bounds, letter = policy.split(' ')
        bounds_tuple = bounds.split('-')
        lower_bound, upper_bound = [int(index) for index in bounds_tuple]

        def filter_fn(x):
            return lower_bound <= x.count(letter) <= upper_bound

        return filter_fn

    return filter_passwords(puzzle_input, generate_filter_fn)


def part_two():
    puzzle_input = get_input()

    def generate_filter_fn(policy):
        indices, letter = policy.split(' ')
        index_tuple = indices.split('-')
        first, last = [int(index) - 1 for index in index_tuple]

        def filter_fn(x):
            return (x[first] == letter) ^ (x[last] == letter)

        return filter_fn

    return filter_passwords(puzzle_input, generate_filter_fn)


print(part_one())
print(part_two())
