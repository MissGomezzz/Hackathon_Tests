import sys

CAP_SOL, REC_SOL = 3, 1      # solicitudes: capacidad 3, recarga 1 por segundo
CAP_TOK, REC_TOK = 100, 20   # tokens de entrada: capacidad 100, recarga 20 por segundo


def techo(a, b):
    return -(-a // b)


def main():
    sol, tok, ultima = CAP_SOL, CAP_TOK, 0
    out = []

    for linea in sys.stdin.read().splitlines():
        p = linea.split()
        if len(p) < 4 or p[0] != "REQUEST":
            continue
        t, nuevos = int(p[1]), int(p[2])  # p[3] (de_cache) no gasta nada

        # Recarga de ambas cubetas hasta el instante t
        dt = t - ultima
        sol = min(CAP_SOL, sol + REC_SOL * dt)
        tok = min(CAP_TOK, tok + REC_TOK * dt)
        ultima = t

        if sol >= 1 and tok >= nuevos:
            sol -= 1
            tok -= nuevos
            out.append("ok")
        else:
            espera = 0
            if sol < 1:
                espera = max(espera, techo(1 - sol, REC_SOL))
            if tok < nuevos:
                espera = max(espera, techo(nuevos - tok, REC_TOK))
            out.append(f"429 retry-after={espera}")

    print("\n".join(out))


main()