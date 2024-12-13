import sys

def main():
    total = 0
    while True:
        a_in = sys.stdin.readline().strip()
        if not a_in:
            break
        a = (int(a_in[12:14]), int(a_in[18:20]))
        b_in = sys.stdin.readline().strip()
        b = (int(b_in[12:14]), int(b_in[18:20]))
        x_in = sys.stdin.readline().strip()
        x = (int(x_in.split('=')[1].split(',')[0]) + 10000000000000, int(x_in.split('=')[2]) + 10000000000000)
        _ = sys.stdin.readline()
        det = a[0]*b[1] - a[1]*b[0]
        if det == 0:
            continue
        n_a = (b[1]*x[0] - b[0]*x[1]) / det
        n_b = (-a[1]*x[0] + a[0]*x[1]) / det
        if abs(n_a - int(n_a)) != 0:#or n_a > 100:
            continue
        if abs(n_b - int(n_b)) != 0:# or n_b > 100:
            continue
        cost = 3*n_a + n_b
        total += int(cost)
    print(total)

if __name__ == '__main__':
    main()