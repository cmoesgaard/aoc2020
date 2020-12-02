def get_input():
    with open('input/2', 'r') as f:
        return [line.strip() for line in f.readlines()]


def parse_line(line):
    policy, password = line.split(': ')
    bounds, letter = policy.split(' ')
    lower, upper = bounds.split('-')
    return int(lower), int(upper), letter, password


def filter_passwords(input_list, filter_fn):
    parsed_input = map(parse_line, input_list)
    filtered = filter(filter_fn, parsed_input)
    return len(list(filtered))


def part_one():
    puzzle_input = get_input()

    def filter_fn(password_tuple):
        lower, upper, letter, password = password_tuple
        return lower <= password.count(letter) <= upper

    return filter_passwords(puzzle_input, filter_fn)


def part_two():
    puzzle_input = get_input()

    def filter_fn(password_tuple):
        lower, upper, letter, password = password_tuple
        return (password[lower - 1] == letter) ^ (password[upper - 1] == letter)

    return filter_passwords(puzzle_input, filter_fn)


print(part_one())
print(part_two())
