def get_input():
    with open('input/5', 'r') as f:
        return [line.strip() for line in f.readlines()]


def parse_input_line(line):
    line = line.replace('B', '1')
    line = line.replace('F', '0')
    line = line.replace('R', '1')
    line = line.replace('L', '0')
    return int(line, 2)


def part_one():
    parsed_input = map(parse_input_line, get_input())
    return max(parsed_input)


def part_two():
    parsed_input = map(parse_input_line, get_input())
    occupied_seats = sorted(parsed_input)

    def filter_seat(i):
        return (
            i not in occupied_seats
            and i - 1 in occupied_seats
            and i + 1 in occupied_seats
        )

    seat_candidates = range(occupied_seats[0], occupied_seats[-1])

    filtered = filter(filter_seat, seat_candidates)
    return next(filtered)


print(part_one())
print(part_two())
