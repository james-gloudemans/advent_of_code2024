import re
import sys

def sum_mul(text: str) -> int:
    pattern = re.compile(r'mul\(([0-9]{1,3}),([0-9]{1,3})\)')
    return sum(a*b for a, b in (map(int, match) for match in pattern.findall(text)))

def main():
    print(sum_mul(sys.stdin.read()))

if __name__ == '__main__':
    main()