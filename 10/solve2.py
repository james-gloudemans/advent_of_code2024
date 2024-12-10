import dataclasses
import sys

@dataclasses.dataclass
class Node:
    pos: tuple[int, int]
    height: int
    visited: bool = False
    score: int | None = None

    def neighbors(self):
        yield (self.pos[0] + 1, self.pos[1])
        yield (self.pos[0] - 1, self.pos[1])
        yield (self.pos[0], self.pos[1] + 1)
        yield (self.pos[0], self.pos[1] - 1)

def dfs(node: Node, top: list[list[Node]]) -> int:
    "Perform a depth first search within `top` starting from `node` and return the score."
    node.visited = True
    if node.height == 9:
        node.score = 1
        return node.score
    node.score = 0
    for n in node.neighbors():
        if n[0] >= 0 and n[1] >= 0 and n[0] < len(top[0]) and n[1] < len(top):
            nxt = top[n[1]][n[0]]
            if nxt.height == node.height + 1:
                if nxt.visited:
                    node.score += nxt.score
                else:
                    node.score += dfs(nxt, top)
    return node.score

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
        total += dfs(head, node_top)
    print(total)

if __name__ == '__main__':
    main()