import collections
import sys

from solve1 import Plot, Region, merge

def num_edges(self) -> int:
        total = 0
        for plot in self.plots:
            p = plot.pos
            # Upper right
            if Plot((p[0]+1, p[1])) in self.plots and Plot((p[0], p[1]+1)) in self.plots and Plot((p[0]+1, p[1]+1)) not in self.plots:
                total += 1
            if Plot((p[0]+1, p[1])) not in self.plots and Plot((p[0], p[1]+1)) not in self.plots:
                total += 1
            # Upper left
            if Plot((p[0]-1, p[1])) in self.plots and Plot((p[0], p[1]+1)) in self.plots and Plot((p[0]-1, p[1]+1)) not in self.plots:
                total += 1
            if Plot((p[0]-1, p[1])) not in self.plots and Plot((p[0], p[1]+1)) not in self.plots:
                total += 1
            # Lower left
            if Plot((p[0]-1, p[1])) in self.plots and Plot((p[0], p[1]-1)) in self.plots and Plot((p[0]-1, p[1]-1)) not in self.plots:
                total += 1
            if Plot((p[0]-1, p[1])) not in self.plots and Plot((p[0], p[1]-1)) not in self.plots:
                total += 1
            # Lower right
            if Plot((p[0]+1, p[1])) in self.plots and Plot((p[0], p[1]-1)) in self.plots and Plot((p[0]+1, p[1]-1)) not in self.plots:
                total += 1
            if Plot((p[0]+1, p[1])) not in self.plots and Plot((p[0], p[1]-1)) not in self.plots:
                total += 1            
        return total

setattr(Region, 'num_edges', num_edges)

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
    print(sum(r.area() * r.num_edges() for regions in region_map.values() for r in regions))

if __name__ == '__main__':
    main()