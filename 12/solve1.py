import collections
import dataclasses
import sys
import typing

@dataclasses.dataclass
class Plot:
    pos: tuple[int, int]

    def is_adjacent(self, other: "Plot") -> bool:
        horizontal = abs(self.pos[0] - other.pos[0]) == 1 and abs(self.pos[1] - other.pos[1]) == 0
        vertical = abs(self.pos[0] - other.pos[0]) == 0 and abs(self.pos[1] - other.pos[1]) == 1
        return horizontal or vertical
    
    def neighbors(self) -> typing.Generator["Plot", None, None]:
        yield Plot((self.pos[0] + 1, self.pos[1]))
        yield Plot((self.pos[0] - 1, self.pos[1]))
        yield Plot((self.pos[0], self.pos[1] + 1))
        yield Plot((self.pos[0], self.pos[1] - 1))

    def __hash__(self) -> int:
        return hash(self.pos)

@dataclasses.dataclass
class Region:
    crop: str
    plots: set[Plot]

    def merge(self, other: "Region") -> None:
        assert self.crop == other.crop
        self.plots.update(other.plots)

    def is_adjacent(self, other: "Region") -> bool:
        return any(p.is_adjacent(o) for p in self.plots for o in other.plots)
    
    def area(self) -> int:
        return len(self.plots)
    
    def perimeter(self) -> int:
        return sum(p not in self.plots for plot in self.plots for p in plot.neighbors())
    
    def price(self) -> int:
        return self.area() * self.perimeter()

def merge(regions: list[Region]) -> list[Region]:
    result: list[Region] = list()
    while True:
        N = len(regions)
        while regions:
            r = regions.pop()
            for s in result:
                if r.is_adjacent(s):
                    s.merge(r)
                    break
            else:
                result.append(r)
        if len(result) == N:
            break
        regions = result.copy()
        result = list()
    return result

def main():
    region_map: dict[str, list[Region]] = collections.defaultdict(list)
    for y, line in enumerate(sys.stdin):
        for x, c in enumerate(line.strip()):
            plot = Plot((x, y))
            region = Region(c, set((plot,)))
            region_map[c].append(region)
    for i, crop in enumerate(region_map):
        print(i, end='\r')
        region_map[crop] = merge(region_map[crop])
    print()
    print(sum(r.price() for regions in region_map.values() for r in regions))

if __name__ == '__main__':
    main()