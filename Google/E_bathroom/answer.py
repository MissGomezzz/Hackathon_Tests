import sys

def main():
    lineas = sys.stdin.read().split("\n")
    t = int(lineas[0])
    out = []
    for caso in range(1, t + 1):
        n, k = map(int, lineas[caso].split())
        conteo = {n: 1}
        while True:
            x = max(conteo)
            c = conteo.pop(x)
            if k <= c:
                out.append(f"Case #{caso}: {x // 2} {(x - 1) // 2}")
                break
            k -= c
            for y in (x // 2, (x - 1) // 2):
                conteo[y] = conteo.get(y, 0) + c
    print("\n".join(out))

main()