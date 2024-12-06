import sys

def rotate(dir: tuple[int, int]) -> tuple[int, int]:
    "Rotate the direction by 90 degrees to the right and return the new direction."
    return (dir[1], -dir[0])

def move(pos: tuple[int, int], dir: tuple[int, int]) -> tuple[int, int]:
    "Move the guard one position in direction `dir` and return the new position."
    return (pos[0] + dir[0], pos[1] - dir[1])

def main():
    pos: tuple[int, int] = (0, 0)
    dir: tuple[int, int] = (0, 1)
    visited: set[tuple[int, int]] = set()
    puzzle = [line.strip() for line in sys.stdin]
    for y, line in enumerate(puzzle):
        for x, c in enumerate(line):
            if c == '^':
                pos = (x, y)
                puzzle[y] = puzzle[y].replace('^', '.')
    while True:
        visited.add(pos)
        m = move(pos, dir)
        if any(c < 0 for c in m) or any(c >= len(puzzle) for c in m):
            break
        if puzzle[m[1]][m[0]] == '#':
            dir = rotate(dir)
        elif puzzle[m[1]][m[0]] == '.':
            pos = m
    print(len(visited))

if __name__ == '__main__':
    main()