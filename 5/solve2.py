import sys

from solve1 import obeys_rule

def fix(update: list[int], rules: list[tuple[int, int]]) -> list[int]:
    result: list[int] = [i for i in update]
    while not all(obeys_rule(result, rule) for rule in rules): # :(
        for rule in rules:
            if not obeys_rule(result, rule):
                result.remove(rule[0])
                result.insert(result.index(rule[1]), rule[0])
    return result
    
def main():
    rules: list[tuple[int, int]] = list()
    for line in sys.stdin:
        if line == '\n':
            break
        rules.append(tuple(map(int, line.split('|'))))
    updates = [[int(page) for page in line.split(',')] for line in sys.stdin]
    rule_breakers = (update for update in updates if not all(obeys_rule(update, rule) for rule in rules))
    total = 0
    for update in rule_breakers:
        u = fix(update, rules)
        total += u[len(u)//2]
    print(total)

if __name__ == '__main__':
    main()