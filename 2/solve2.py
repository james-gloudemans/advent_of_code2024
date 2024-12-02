import itertools
import sys

def is_safe(report: list[int]) -> bool:
    inc = all(0 < (b - a) < 4 for a, b in itertools.pairwise(report))
    dec = all(0 < (a - b) < 4 for a, b in itertools.pairwise(report))
    return inc or dec

def main():
    total = 0
    for line in sys.stdin:
        report = [int(num) for num in line.split()]
        reports = [report,] + [report[:i] + report[i+1:] for i,_ in enumerate(report)]
        if any(is_safe(rep) for rep in reports):
            total += 1
    print(f'total safe reports: {total}')

if __name__ == '__main__':
    main()