from typing import List
from typing import Dict


def logic_gate(wire1: int, wire2: int, op: str) -> int:
    if op == "AND":
        return wire1 & wire2
    elif op == "OR":
        return wire1 | wire2
    elif op == "XOR":
        return wire1 ^ wire2


def part1(wires: Dict[str, int], gates: List[str]) -> int:
    while gates:
        temp = gates.pop(0)
        gate = temp.split(" ")
        if gate[0] in wires and gate[2] in wires:
            wires[gate[4]] = logic_gate(wires[gate[0]], wires[gate[2]], gate[1])
        else:
            gates.append(temp)
    wires = dict(sorted(wires.items(), reverse=True))
    ans = ""
    for k, v in wires.items():
        if k.startswith("z"):
            ans += str(v)
        else:
            break
    print(int(ans, 2))
    return 0



def part2(wires: Dict[str, str], gates: List[str]) -> int:
    return 0


if __name__ == "__main__":
    with open('inputs/in24.txt', 'r') as f:
        ok, wires, gates = True, {}, []
        for lines in f:
            if lines == '\n':
                ok = False
                continue
            if ok:
                wire, input = lines.strip().split(": ")
                wires[wire] = int(input)
            else:
                gates.append(lines.strip())
    f.close()


    print("Day 24:")
    print(part1(wires, gates))
    print(part2(wires, gates))
    