from more_itertools import split_at, flatten


def get_input():
    with open('input/4', 'r') as f:
        return [line.strip() for line in f.readlines()]


def validate(passport):
    def hgt_strategy(hgt):
        height, unit = hgt[:-2], hgt[-2:]

        if not height.isdigit() or unit not in {'cm', 'in'}:
            return False

        if unit == 'cm':
            return 150 <= int(height) <= 193
        if unit == 'in':
            return 59 <= int(height) <= 76

    def hcl_strategy(hcl):
        head, tail = hcl[:1], hcl[1:]
        if head != '#':
            return False
        try:
            int(tail, 16)
        except ValueError:
            return False
        return True

    strategies = {
        'byr': lambda byr: len(byr) == 4 and 1920 <= int(byr) <= 2002,
        'iyr': lambda iyr: len(iyr) == 4 and 2010 <= int(iyr) <= 2020,
        'eyr': lambda eyr: len(eyr) == 4 and 2020 <= int(eyr) <= 2030,
        'hgt': hgt_strategy,
        'hcl': hcl_strategy,
        'ecl': lambda ecl: ecl in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"},
        'pid': lambda pid: len(pid) == 9 and pid.isdigit(),
    }

    def run_strategy(passport_tuple):
        k, v = passport_tuple
        return strategies[k](v)

    validated = map(run_strategy, passport.items())
    return all(validated)


def process_input(input_str):
    passports = split_at(input_str, lambda x: x == '')

    def process_passports(passport):
        fields = flatten(map(lambda x: x.split(' '), passport))
        split_fields = map(lambda x: x.split(':'), fields)
        filtered = filter(lambda x: x[0] != 'cid', split_fields)
        return dict(filtered)

    return map(process_passports, passports)


def filter_missing_keys(passport):
    keys = set(passport.keys())
    wanted_keys = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    difference = wanted_keys.difference(keys)
    return not difference


def part_one():
    chunked_input = process_input(get_input())
    no_missing_keys = filter(filter_missing_keys, chunked_input)
    return len(list(no_missing_keys))


def part_two():
    chunked_input = process_input(get_input())
    no_missing_keys = filter(filter_missing_keys, chunked_input)
    validated = filter(validate, no_missing_keys)
    return len(list(validated))


print(part_one())
print(part_two())
