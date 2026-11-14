import sys

def main():
    tokens = sys.stdin.read().split()
    pos = 0
    t = int(tokens[pos]); pos += 1
    out = []
    for caso in range(1, t + 1):
        n = int(tokens[pos]); pos += 1
        acts = []
        for i in range(n):
            s = int(tokens[pos]); e = int(tokens[pos + 1])
            pos += 2
            acts.append((s, e, i))
        acts.sort()
        res = [""] * n
        fin_c = fin_j = 0
        posible = True
        for s, e, i in acts:
            if fin_c <= s:
                res[i] = "C"
                fin_c = e
            elif fin_j <= s:
                res[i] = "J"
                fin_j = e
            else:
                posible = False
                break
        out.append(f"Case #{caso}: " + ("".join(res) if posible else "IMPOSSIBLE"))
    print("\n".join(out))

main()