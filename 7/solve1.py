import itertools
import operator
import sys

def main():
    total = 0
    for i, line in enumerate(sys.stdin):
        print(f'{i+1}', end='\r')
        eq = line.split(':')
        target = int(eq[0])
        nums = [int(n) for n in eq[1].split()]
        for op in map(list, itertools.product([operator.mul, operator.add], repeat=len(nums)-1)):
            acc = nums[0]
            for n in nums[1:]:
                acc = op.pop()(acc, n)
            if acc == target:
                total += target
                break
    print()
    print(total)

if __name__ == '__main__':
    main()