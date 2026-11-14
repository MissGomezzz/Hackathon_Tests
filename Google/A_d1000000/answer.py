import sys

def main():
    tokens = sys.stdin.read().split()
    pos = 0
    t = int(tokens[pos]); pos += 1
    out = []
    for caso in range(1, t + 1):
        n = int(tokens[pos]); pos += 1
        caras = sorted(int(x) for x in tokens[pos:pos + n])
        pos += n
        largo = 0
        for s in caras:
            if s > largo:
                largo += 1
        out.append(f"Case #{caso}: {largo}")
    print("\n".join(out))

main()