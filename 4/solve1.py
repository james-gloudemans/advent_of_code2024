import re
import sys
import typing

def diags(x: list[str]) -> typing.Generator[str, None, None]:
    '''Yield all of the diagonals of 2D list of strings `x`'''
    N = len(x)
    # Center diagonal
    yield ''.join(x[i][i] for i in range(N))
    # Upper diagonals
    for i in range(N-1):
        yield ''.join(x[j][k] for j, k in enumerate(range(i+1, N)))
    # Lower diagonals
    for i in range(1, N):
        yield ''.join(x[i+j][k] for j, k in enumerate(range(N-i)))

def count_xmas(text: str) -> int:
    '''Count the number of occurences of 'XMAS' in `text` including overlapping'''
    pattern = re.compile(r'(?=XMAS)')
    return len(pattern.findall(text)) + len(pattern.findall(''.join(reversed(text))))

def search_patterns(puzzle: list[str]) -> typing.Generator[str, None, None]:
    for row in puzzle:
        yield row
    for col in zip(*puzzle):
        yield ''.join(col)
    yield from diags(puzzle)
    yield from diags([list(reversed(row)) for row in puzzle])

def main():
    print(sum(count_xmas(chunk) for chunk in search_patterns(sys.stdin.read().splitlines())))

if __name__ == '__main__':
    main()