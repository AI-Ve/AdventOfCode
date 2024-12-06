from typing import List
from operator import add


_DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def part1(lines: List[List[str]]) -> int:
    _R, _C = len(lines), len(lines[0])
    position = None
    for i in range(_R):
        for j in range(_C):
            if lines[i][j] == '^':
                position = [i, j]

    orientation = 0
    visited = set()
    visited.add(tuple(position))

    while True:
        dr, dc = _DIRECTIONS[orientation]
        front = (position[0] + dr, position[1] + dc)
        if 0 <= front[0] < _R and 0 <= front[1] < _C and lines[front[0]][front[1]] == "#":
            orientation = (orientation + 1) % 4
        else:
            position = (position[0] + dr, position[1] + dc)
            if not (0 <= position[0] < _R and 0 <= position[1] < _C):
                break

            visited.add(position)

    return len(visited)
    

def part2(lines: List[List[str]]) -> int:
    return 0


if __name__ == "__main__":
    with open('day06/input.in', 'r') as f:
        lines = [[x for x in l.strip()] for l in f.readlines()]
        
        f.close()
    
    print(f"Day 06 answers: ")
    print(part1(lines))
    print(part2(lines))