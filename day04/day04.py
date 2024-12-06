def part1() -> int:
    pass


def part2() -> int:
    pass


if __name__ == "__main__":
    with open("day04/test_input.in", 'r') as f:
        lines = [x.strip() for x in f.readlines()]
        f.close()
    
    print(part1(lines))
    print(part2(lines))