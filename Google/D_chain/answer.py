import sys

def main():
    tokens = sys.stdin.read().split()
    pos = 0
    t = int(tokens[pos]); pos += 1
    out = []
    for caso in range(1, t + 1):
        n = int(tokens[pos]); pos += 1
        f = [int(x) for x in tokens[pos:pos + n]]; pos += n
        p = [int(x) for x in tokens[pos:pos + n]]; pos += n

        hijos = [[] for _ in range(n + 1)]
        for i in range(1, n + 1):
            hijos[p[i - 1]].append(i)

        mejor = [0] * (n + 1)
        total = 0
        for i in range(n, 0, -1):
            if not hijos[i]:
                mejor[i] = f[i - 1]
            else:
                vals = [mejor[k] for k in hijos[i]]
                m = min(vals)
                total += sum(vals) - m
                mejor[i] = max(f[i - 1], m)
        for k in hijos[0]:
            total += mejor[k]

        out.append(f"Case #{caso}: {total}")
    print("\n".join(out))

main()