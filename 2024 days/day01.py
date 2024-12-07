from typing import List

def part1(lines: List[List[str]]) -> int:
    l1, l2 = [], []
    for line in lines:
        line = list(map(int, line))
        l1.append(line[0])
        l2.append(line[1])
    
    l1.sort()
    l2.sort()
    
    return sum([abs(i - j) for i, j in zip(l1, l2)])


def part2(lines: List[List[str]]) -> int:
    l1, l2 = [], []
    for line in lines:
        line = list(map(int, line))
        l1.append(line[0])
        l2.append(line[1])

    d = {}
    for i in l1:
        d[i] = l2.count(i)
    
    return sum([k * v for k, v in d.items()])


if __name__ == "__main__":
    with open('inputs/in01.txt', 'r') as f:
        lines = [l.split() for l in f.readlines()]
        f.close()

    print("Day 01:")
    print(part1(lines))
    print(part2(lines))