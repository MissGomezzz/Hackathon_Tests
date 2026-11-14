import sys

def main():
    lineas = sys.stdin.read().splitlines()
    t = int(lineas[0])
    out = []
    INF = float("inf")
    for caso in range(1, t + 1):
        x, y, s = lineas[caso].split()
        x, y = int(x), int(y)
        dc = dj = INF
        for i, ch in enumerate(s):
            if i == 0:
                nc = 0 if ch != "J" else INF
                nj = 0 if ch != "C" else INF
            else:
                nc = min(dc, dj + y) if ch != "J" else INF
                nj = min(dj, dc + x) if ch != "C" else INF
            dc, dj = nc, nj
        out.append(f"Case #{caso}: {min(dc, dj)}")
    print("\n".join(out))

main()