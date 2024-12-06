import sys

def obeys_rule(line: list[int], rule: tuple[int, int]) -> bool:
    return rule[0] not in line or rule[1] not in line or line.index(rule[0]) < line.index(rule[1])

def main():
    rules: list[tuple[int, int]] = list()
    for line in sys.stdin:
        if line == '\n':
            break
        rules.append(tuple(map(int, line.split('|'))))
    updates = [[int(page) for page in line.split(',')] for line in sys.stdin]
    # assume no pages are duplicated in any update
    assert all(len(set(update)) == len(update) for update in updates)
    print(sum(update[len(update)//2] for update in updates if all(obeys_rule(update, rule) for rule in rules)))

if __name__ == '__main__':
    main()