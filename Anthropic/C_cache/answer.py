import sys
import json


def dolares(m):
    # m está en millonésimas de dólar (entero)
    return f"${m // 1_000_000}.{m % 1_000_000:06d}"


def main():
    out = []
    total = sin_cache = aciertos = n = 0

    for linea in sys.stdin.read().splitlines():
        if not linea.strip():
            continue
        u = json.loads(linea)
        entrada = u["input_tokens"]
        creacion = u["cache_creation_input_tokens"]
        lectura = u["cache_read_input_tokens"]
        salida = u["output_tokens"]

        # Precios por token x100: entrada 300, escritura 375, lectura 30, salida 1500
        costo = (entrada * 300 + creacion * 375 + lectura * 30 + salida * 1500) // 100
        sin = (entrada + creacion + lectura) * 3 + salida * 15

        n += 1
        total += costo
        sin_cache += sin
        if lectura > 0:
            aciertos += 1
        out.append(f"solicitud {n}: {dolares(costo)}")

    out.append(f"total: {dolares(total)}")
    out.append(f"sin_cache: {dolares(sin_cache)}")
    out.append(f"ahorro: {dolares(sin_cache - total)}")
    out.append(f"aciertos_de_cache: {aciertos}/{n}")
    print("\n".join(out))


main()