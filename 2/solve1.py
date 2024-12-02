import itertools
import sys

def is_safe(report: list[int]) -> bool:
    inc = all(0 < (b - a) < 4 for a, b in itertools.pairwise(report))
    dec = all(0 < (a - b) < 4 for a, b in itertools.pairwise(report))
    return inc or dec

def main():
    reports = ([int(num) for num in line.split()] for line in sys.stdin)
    total = sum(is_safe(report) for report in reports)
    print(f'total safe reports: {total}')

if __name__ == '__main__':
    main()