from typing import List

def check_valid(line: List[int]) -> bool:
    direction = -1 if line[0] - line[1] < 0 else 1 if line[0] - line[1] else 0

    for i in range(len(line) - 1):
        if direction == 0: 
            return False
        if not 1 <= (line[i] - line[i + 1]) * direction <= 3:
            return False
    return True

def part1() -> int:
    ans = 0

    for line in lines:
        if check_valid(line):
            ans += 1
    
    return ans


def part2() -> int:
    ans = 0

    for line in lines:
        if check_valid(line):
            ans += 1
        else:
            for i in range(len(line)):
                new_line = line[:i] + line[i + 1:]
                if check_valid(new_line):
                    ans += 1
                    break 
    
    return ans
    
    

if __name__ == "__main__":
    with open('inputs/in02.txt', 'r') as f:
        lines = [l.split() for l in f.readlines()]  
        lines = [[int(x) for x in l] for l in lines]
        f.close()

    print("Day02: ")
    print(part1())
    print(part2())   