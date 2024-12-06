import sys

def rotate(dir: tuple[int, int]) -> tuple[int, int]:
    "Rotate the direction by 90 degrees to the right and return the new direction."
    return (dir[1], -dir[0])

def move(pos: tuple[int, int], dir: tuple[int, int]) -> tuple[int, int]:
    "Move the guard one position in direction `dir` and return the new position."
    return (pos[0] + dir[0], pos[1] - dir[1])

def has_cycle(puzzle: list[str], start: tuple[int, int]) -> bool:
    "Does `puzzle` have a cycle if the guard starts at `start`"
    pos = start
    dir: tuple[int, int] = (0, 1)
    visited: set[tuple[int, int, int, int]] = set()
    while True:
        if (pos[0], pos[1], dir[0], dir[1]) in visited:
            return True
        visited.add((pos[0], pos[1], dir[0], dir[1]))
        m = move(pos, dir)
        if any(c < 0 for c in m) or any(c >= len(puzzle) for c in m):
            break
        if puzzle[m[1]][m[0]] == '#':
            dir = rotate(dir)
        elif puzzle[m[1]][m[0]] == '.':
            pos = m
    return False

def main():
    pos: tuple[int, int] = (0, 0)
    puzzle: list[str] = [line.strip() for line in sys.stdin]
    for y, line in enumerate(puzzle):
        for x, c in enumerate(line):
            if c == '^':
                pos = (x, y)
                puzzle[y] = puzzle[y].replace('^', '.')
    total: int = 0
    for y, line in enumerate(puzzle):
        for x, c in enumerate(line):
            if (x, y) != pos and puzzle[y][x] == '.':
                p = [s for s in puzzle]
                p[y] = p[y][:x] + '#' + p[y][x+1:]
                total += has_cycle(p, pos)
        print(f'{y+1} / {len(puzzle)}', end='\r')
    print(f'\n{total}')

if __name__ == '__main__':
    main()