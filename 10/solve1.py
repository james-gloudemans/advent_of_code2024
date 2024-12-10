import dataclasses
import sys

@dataclasses.dataclass
class Node:
    pos: tuple[int, int]
    height: int
    visited: bool = False

    def neighbors(self):
        yield (self.pos[0] + 1, self.pos[1])
        yield (self.pos[0] - 1, self.pos[1])
        yield (self.pos[0], self.pos[1] + 1)
        yield (self.pos[0], self.pos[1] - 1)

def dfs(node: Node, top: list[list[Node]]) -> set[tuple[int, int]]:
    "Perform a depth first search within `top` starting from `node` and return the score."
    node.visited = True
    if node.height == 9:
        return set((node.pos,))
    reachable: set[tuple[int, int]] = set()
    for n in node.neighbors():
        if n[0] >= 0 and n[1] >= 0 and n[0] < len(top[0]) and n[1] < len(top):
            nxt = top[n[1]][n[0]]
            if not nxt.visited and nxt.height == node.height + 1:
                reachable.update(dfs(nxt, top))
    return reachable

def main():
    node_top: list[list[Node]] = [[Node((x, y), int(h))
                                                 for x, h in enumerate(line.strip())]
                                                 for y, line in enumerate(sys.stdin)]
    trailheads = list()
    for row in node_top:
        for node in row:
            if node.height == 0:
                trailheads.append(node)
    trailheads = tuple(trailheads)
    total = 0
    for head in trailheads:
        for row in node_top:
            for node in row:
                node.visited = False
        total += len(dfs(head, node_top))
    print(total)

if __name__ == '__main__':
    main()