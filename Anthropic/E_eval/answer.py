import sys
import json
import re
import unicodedata


def normalizar(s):
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", " ", s)
    return s.strip()


def main():
    sys.stdin.reconfigure(encoding="utf-8")
    sys.stdout.reconfigure(encoding="utf-8")

    cats = {}
    aprobadas = total = 0

    for linea in sys.stdin.read().splitlines():
        if not linea.strip():
            continue
        d = json.loads(linea)
        esperado = normalizar(d["esperado"])
        respuesta = normalizar(d["respuesta"])
        paso = f" {esperado} " in f" {respuesta} "

        c = cats.setdefault(d["categoria"], [0, 0])
        c[1] += 1
        total += 1
        if paso:
            c[0] += 1
            aprobadas += 1

    out = [f"{cat}: {a}/{n}" for cat, (a, n) in sorted(cats.items())]
    pct = aprobadas * 100 / total if total else 0.0
    out.append(f"total: {aprobadas}/{total} ({pct:.1f}%)")
    print("\n".join(out))


main()