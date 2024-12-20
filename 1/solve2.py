import collections
import sys

def main():
    total: int = 0
    left = collections.Counter()
    right = collections.Counter()
    for line in sys.stdin:
        nums = line.split()
        left[int(nums[0])] += 1
        right[int(nums[1])] += 1
    total = sum(num*count*right[num] for num, count in left.items())
    print(f'similarity score: {total}')

if __name__ == '__main__':
    main()