import sys

def is_safe(report: list[int]) -> bool:
    inc = all(0 < (b - a) < 4 for a, b in zip(report, report[1:]))
    dec = all(0 < (a - b) < 4 for a, b in zip(report, report[1:]))
    return inc or dec

def main():
    reports = ([int(num) for num in line.split()] for line in sys.stdin)
    total = sum(is_safe(report) for report in reports)
    print(f'total safe reports: {total}')

if __name__ == '__main__':
    main()