import itertools
import sys

type Block = tuple[int | None, int]

def checksum(disk: list[Block]) -> int:
    i: int = 0
    total: int = 0
    for block in disk:
        for _ in range(block[1]):
            if block[0] is not None:
                total += i*block[0]
            i += 1
    return total

def index_block(disk: list[Block], fileID: int) -> int:
    "Return the index of the block associated with `fileID`"
    for i, block in enumerate(disk):
        if block[0] == fileID:
            return i
    raise ValueError(f'index_block: block not found: {fileID}')

def remove_block(disk: list[Block], fileID: int) -> Block:
    "Remove and return the block associated with `fileID`"
    i = index_block(disk, fileID)
    block = disk[i]
    new_block = [None, block[1]]
    if i > 0 and disk[i-1][0] is None:
        new_block[1] += disk[i-1][1]
        del disk[i-1]
        i -= 1
    if i < len(disk)-1 and disk[i+1][0] is None:
        new_block[1] += disk[i+1][1]
        del disk[i+1]
    disk[i] = tuple(new_block)
    return block

def main():
    disk_map = [int(n) for n in sys.stdin.read().strip()]
    disk_map.append(0)
    disk: list[Block] = list()
    for i, (full, empty) in enumerate(itertools.batched(disk_map, n=2)):
        disk.append((i, full))
        if empty > 0:
            disk.append((None, empty))
    # Assume no zero-length blocks
    assert not any(b[1] == 0 for b in disk)
    N_files = len(disk_map)//2
    for i in reversed(range(1, N_files)):
        print(f'{i} / {N_files}', end='\r')
        idx = index_block(disk, i)
        for j, free_block in enumerate(disk):
            if free_block[0] is not None:
                continue
            if j > idx:
                break
            if free_block[1] >= disk[idx][1]:
                block = remove_block(disk, i)
                free_block = disk[j]
                disk.insert(j, block)
                new_free_block = (None, free_block[1] - block[1])
                if new_free_block[1] > 0:
                    disk[j+1] = new_free_block
                else:
                    del disk[j+1]
                break
    # Check assumption: there are no adjacent pairs of free blocks
    for first, second in itertools.pairwise(disk):
        assert not (first[0] is None and second[0] is None)
    # Assume no zero-length blocks
    assert not any(b[1] == 0 for b in disk)
    print()
    print(disk)
    print(checksum(disk))

if __name__ == '__main__':
    main()