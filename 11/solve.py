import functools
import sys

@functools.cache
def blink(stone: str, N: int) -> int:
    if N == 0:
        return 1
    elif stone == '0':
        return blink('1', N-1)
    elif len(stone) % 2 == 0:
        mid = len(stone)//2
        return blink(stone[:mid], N-1) + blink(stone[mid:].lstrip('0') or '0', N-1)
    else:
        return blink(str(int(stone)*2024), N-1)

def main():
    N_blinks = int(sys.argv[1])
    print(sum(blink(stone, N_blinks) for stone in sys.stdin.read().strip().split()))

if __name__ == '__main__':
    main()