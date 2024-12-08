import collections
import itertools
import sys

from solve1 import Point

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
            node = p1
            diff = p1 - p2
            while node in edge:
                nodes.add(node)
                node = node + diff
    print(len(nodes))

if __name__ == '__main__':
    main()