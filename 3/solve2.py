import sys

from solve1 import sum_mul

def main():
    memory = sys.stdin.read().split('do()')
    print(sum(sum_mul(chunk.split('don\'t()')[0]) for chunk in memory))

if __name__ == '__main__':
    main()