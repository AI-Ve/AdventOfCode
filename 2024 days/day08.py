from typing import List
from typing import Tuple
from collections import defaultdict
from itertools import permutations


def show_matrix(lines: List[List[str]]) -> None:
    _ROWS, _COLS = len(lines), len(lines[0])

    for i in range(_ROWS):
        for j in range(_COLS):
            print(lines[i][j], end = "")
        print()


def mirror_point(point: Tuple[int, int], ref: Tuple[int, int]) -> Tuple[int, int]:
    return (2 * ref[0] - point[0], 2 * ref[1] - point[1])


def part1(lines: List[List[str]]) -> int:
    antenas = defaultdict(list)
    _ROWS, _COLS = len(lines), len(lines[0])
    nodes, ans = [], 0

    for i in range(_ROWS):
        for j in range(_COLS):
            if lines[i][j] != '.':
                antenas[lines[i][j]].append((i, j))

    antenas_loc = [a for v in antenas.values() for a in v]

    for v in antenas.values():
        for pair in (permutations(v, 2)):
            nodes.append(mirror_point(pair[0], pair[1]))

    for i in range(_ROWS):
        for j in range(_COLS):
            if (i, j) in nodes:
                ans += 1

    return ans


def part2(lines: List[List[str]]) -> int:
    antenas = defaultdict(list)
    _ROWS, _COLS = len(lines), len(lines[0])
    nodes, ans = [], 0

    for i in range(_ROWS):
        for j in range(_COLS):
            if lines[i][j] != '.':
                antenas[lines[i][j]].append((i, j))

    antenas_loc = [a for v in antenas.values() for a in v]

    for v in antenas.values():
        for pair in (permutations(v, 2)):
            p1, p2 = pair
            while True:
                m = mirror_point(p1, p2)
                if 0 <= m[0] < _ROWS and 0 <= m[1] < _COLS:
                    nodes.append(m)
                    p1, p2 = p2, m
                else:
                    break

    for i in range(_ROWS):
        for j in range(_COLS):
            if (i, j) in nodes:
                lines[i][j] = '#'
                ans += 1
            if lines[i][j] not in ['.', '#']:
                ans += 1

    return ans


if __name__ == "__main__":
    with open('inputs/in08.txt', 'r') as f:
        lines = [[x for x in line.strip()] for line in f.readlines()]
        f.close()


    print("Day 8: ")
    print(part1(lines))
    print(part2(lines))