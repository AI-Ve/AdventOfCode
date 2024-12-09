from typing import List
from itertools import batched
import time


def part1(line: List[int]) -> int:
    disk = ""
    occupied, free = [], []
    temp = 0
    for e, i in enumerate(batched(line, 2)):
        disk += str(e) * i[0] + '.' * i[1]
        for k in range(i[0]):
            occupied += [[k + temp, e]]
        for k in range(i[0] + temp, i[0] + i[1] + temp):
            free.append(k)
        temp += i[0] + i[1]

    temp = 0
    occupied.sort(key=lambda x: -x[0])
    while min(free) < max([x[0] for x in occupied]):
        occupied[temp][0], free[temp] = free[temp], occupied[temp][0]
        temp += 1

    ans = 0
    for e, i in enumerate(sorted(occupied, key= lambda x: x[0])):
        ans += e * i[1]

    return ans

def part2(lines: List[int]) -> int:
    disk = ""
    occupied, free = [], []
    temp = 0
    for e, i in enumerate(batched(line, 2)):
        disk += str(e) * i[0] + '.' * i[1]
        for k in range(i[0]):
            occupied += [[k + temp, e]]
        for k in range(i[0]+temp, i[0] + i[1] + temp):
            free.append(k)
        temp += i[0] + i[1]

    print(disk)

    return 0


if __name__ == "__main__":
    with open('inputs/in09test.txt', 'r') as f:
        line = [int(x) for x in f.readline().strip()]
        line.append(0)
        f.close()

    print("Day 9: ")
    print(part1(line))
    # print(part2(line))