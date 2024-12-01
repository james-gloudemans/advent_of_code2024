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
    for num, count in left.items():
        total += num*count*right[num]
    print(f'similarity score: {total}')

if __name__ == '__main__':
    main()