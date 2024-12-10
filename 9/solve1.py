import itertools
import sys

type Disk = list[int | None]

def index_last_num(lst: Disk) -> int:
    "Return the index of the last number in `lst` where the number is in [0, `max`)"
    i = len(lst) - 1
    while lst[i] is None:
        i -= 1
    return i

def next_none(lst: Disk, i) -> int:
    "Return the index of the next `None` entry in `lst[i:]`"
    while lst[i] is not None:
        i += 1
    return i

def checksum(blocks: Disk) -> int:
    return sum(i*n for i, n in enumerate(blocks) if n is not None)

def main():
    disk_map = sys.stdin.read().strip()
    disk_blocks = [0 for _ in range(int(disk_map[0]))]
    block = 1
    for free, file in itertools.batched(disk_map[1:], n=2):
        disk_blocks.extend([None for _ in range(int(free))])
        disk_blocks.extend([block for _ in range(int(file))])
        block += 1
    i = next_none(disk_blocks, 0)
    while any(n is not None for n in disk_blocks[i+1:]):
        file_i = index_last_num(disk_blocks)
        disk_blocks[i], disk_blocks[file_i] = disk_blocks[file_i], None
        i = next_none(disk_blocks, i+1)
    print(checksum(disk_blocks))

if __name__ == '__main__':
    main()