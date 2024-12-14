import functools
import operator
import sys

type Vec = tuple[int, int]

def main():
    robots: list[tuple[Vec, Vec]] = list()
    # walls = (11, 7)
    walls = (101, 103)
    seconds = 100
    quads = [0 for _ in range(4)]
    for line in sys.stdin:
        pieces = line.strip().split('=')
        pos = pieces[1].split(',')
        posy = pos[1].split(' ')[0]
        pos = (int(pos[0]), int(posy))
        v = tuple(int(n) for n in pieces[2].split(','))
        robots.append((pos, v))
    for robot in robots:
        for _ in range(seconds):
            robot = ((robot[0][0] + robot[1][0], robot[0][1] + robot[1][1]), robot[1])
            robot = ((robot[0][0] % walls[0], robot[0][1] % walls[1]), robot[1])
        if robot[0][0] < walls[0]//2 and robot[0][1] < walls[1]//2:
            quads[0] += 1
        if robot[0][0] > walls[0]//2 and robot[0][1] < walls[1]//2:
            quads[1] += 1
        if robot[0][0] < walls[0]//2 and robot[0][1] > walls[1]//2:
            quads[2] += 1
        if robot[0][0] > walls[0]//2 and robot[0][1] > walls[1]//2:
            quads[3] += 1
    print(functools.reduce(operator.mul, quads))

if __name__ == '__main__':
    main()