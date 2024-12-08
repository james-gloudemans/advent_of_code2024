import collections
import itertools
import sys

class Point:

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f'Point({self.x}, {self.y})'
    
    def __str__(self) -> str:
        return f'({self.x}, {self.y})'
    
    def __add__(self, other: "Point") -> "Point":
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other: "Point") -> "Point":
        return Point(self.x - other.x, self.y - other.y)
    
    def __contains__(self, other: "Point") -> bool:
        return other.x < self.x and other.y < self.y and other.y >=0 and other.x >= 0
    
    def __eq__(self, other: "Point") -> bool:
        return self.x == other.x and self.y == other.y
    
    def __hash__(self) -> int:
        return hash((self.x, self.y))

def main():
    puzzle = [line.strip() for line in sys.stdin]
    antennae: dict[str, list[Point]] = collections.defaultdict(list)
    for y, line in enumerate(puzzle):
        for x, c in enumerate(line):
            if c != '.':
                antennae[c].append(Point(x, y))
    edge = Point(len(puzzle[0]), len(puzzle))
    nodes: set[Point] = set()
    for freq, locs in antennae.items():
        for p1, p2 in itertools.permutations(locs, 2):
            node = p1 + p1 - p2
            if node in edge:
                nodes.add(node)
    print(len(nodes))

if __name__ == '__main__':
    main()