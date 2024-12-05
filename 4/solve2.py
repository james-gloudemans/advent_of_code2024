import collections
import itertools
import sys
import typing

def sliding_window(iterable, n):
    "Collect data into overlapping fixed-length chunks or blocks."
    # copied from https://docs.python.org/3.12/library/itertools.html
    # sliding_window('ABCDEFG', 4) → ABCD BCDE CDEF DEFG
    iterator = iter(iterable)
    window = collections.deque(itertools.islice(iterator, n - 1), maxlen=n)
    for x in iterator:
        window.append(x)
        yield list(window)

def search_patterns(puzzle: str) -> typing.Generator[list[str], None, None]:
    for a in sliding_window(puzzle, 3):
        for b in sliding_window(zip(*a), 3):
            yield [''.join(row) for row in zip(*b)]

def is_xmas(chunk) -> bool:
    diag = ''.join(chunk[i][i] for i in range(len(chunk)))
    chunk_transpose = [list(reversed(row)) for row in chunk]
    cdiag = ''.join(chunk_transpose[i][i] for i in range(len(chunk)))
    return (diag == 'MAS' or diag == 'SAM') and (cdiag == 'MAS' or cdiag == 'SAM')

def main():
    puzzle = sys.stdin.read().splitlines()
    print(sum(is_xmas(chunk) for chunk in search_patterns(puzzle)))


if __name__ == '__main__':
    main()