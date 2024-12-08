import re

def interpret(line: str) -> int:
    nrs = re.findall(r'\d+', line)
    nrs = [int(x) for x in nrs]
    return nrs[0] * nrs[1]


def part1() -> int:
    matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)", lines)
    return sum([interpret(m) for m in matches])


def part2() -> int:
    matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)", lines)
    fin = []
    ok = True
    for m in matches:
        if m == 'don\'t()':
            ok = False
        elif m == 'do()':
            ok = True
        if ok and m not in ['don\'t()', 'do()']:
            fin.append(m)
    return sum([interpret(m) for m in fin])


if __name__ == "__main__":
    with open('../inputs/in03.txt', 'r') as f:
        lines = "".join([line.strip() for line in f.readlines()])
        f.close()

    print("Day 03: " )
    print(part1())
    print(part2())   