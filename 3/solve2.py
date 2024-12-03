import re
import sys

def sum_mul(text: str) -> int:
    pattern = re.compile(r'mul\(([0-9]{1,3}),([0-9]{1,3})\)')
    return sum(a*b for a, b in (map(int, match) for match in pattern.findall(text)))

def main():
    memory = sys.stdin.read().split('do()')
    print(sum(sum_mul(chunk.split('don\'t()')[0]) for chunk in memory))

if __name__ == '__main__':
    main()