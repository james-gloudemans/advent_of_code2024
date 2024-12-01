import queue
import sys

def main():
    total = 0
    left: queue.PriorityQueue[int] = queue.PriorityQueue()
    right: queue.PriorityQueue[int] = queue.PriorityQueue()
    for line in sys.stdin:
        nums = line.split()
        left.put(int(nums[0]))
        right.put(int(nums[1]))
    while not left.empty():
        total += abs(left.get() - right.get())
    print(f'total distance: {total}')

if __name__ == '__main__':
    main()