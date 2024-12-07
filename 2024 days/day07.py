from typing import List
from itertools import product


def part1(lines: List[List[str]]) -> int:
    ans = []
    for line in lines:

        target = int(line[0])
        arr = [int(x) for x in line[1].split()]

        for seq in list(product(["+", "*"], repeat = len(arr) - 1)):
            result = arr[0]
            for item, op in zip(arr[1:], seq):
                if op == '+':
                    result += item
                elif op == "*":
                    result *= item
            if result == target:
                ans.append(target)
                break

    return sum(ans)


def part2(lines: List[List[str]]) -> int:
    ans = []
    for line in lines:

        target = int(line[0])
        arr = [int(x) for x in line[1].split()]

        for seq in list(product(["+", "*", "||"], repeat = len(arr) - 1)):
            result = arr[0]
            for item, op in zip(arr[1:], seq):
                if op == '+':
                    result += item
                elif op == "*":
                    result *= item
                elif op == "||":
                    result = int(''.join([str(result), str(item)]))
            if result == target:
                ans.append(target)
                break

    return sum(ans)


if __name__ == "__main__":
    with open('inputs/in07.txt', 'r') as f:
        lines = [l.strip().split(':') for l in f.readlines()]
        f.close()
    
    print(f"Day 07:")
    print(part1(lines))
    print(part2(lines))