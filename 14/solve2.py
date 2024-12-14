import statistics
import sys

type Vec = tuple[int, int]

def spread(pos: list[Vec]) -> float:
    return statistics.stdev([p[0]**2 + p[1]**2 for p in pos])

def main():
    robots: list[tuple[Vec, Vec]] = list()
    walls = (101, 103)
    for line in sys.stdin:
        pieces = line.strip().split('=')
        pos = pieces[1].split(',')
        posy = pos[1].split(' ')[0]
        pos = (int(pos[0]), int(posy))
        v = tuple(int(n) for n in pieces[2].split(','))
        robots.append((pos, v))
    seconds: int = 0
    spreads: list[float] = list()
    while True:
        seconds += 1
        for i, robot in enumerate(robots):
            robot = ((robot[0][0] + robot[1][0], robot[0][1] + robot[1][1]), robot[1])
            robot = ((robot[0][0] % walls[0], robot[0][1] % walls[1]), robot[1])
            robots[i] = robot
        s = spread([r[0] for r in robots])
        spreads.append(s)
        print(seconds, end='\r')
        if seconds > 100 and s < statistics.mean(spreads[-100:]) - 7*statistics.stdev(spreads[-100:]):
            break
    print()
    print(seconds)

if __name__ == '__main__':
    main()