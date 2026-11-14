import sys
import json

CIUDADES = {"Bogotá": 14, "Medellín": 24, "Cali": 26}


def calculadora(inp):
    op, a, b = inp.get("operacion"), inp.get("a"), inp.get("b")
    if op == "sumar":
        return str(a + b)
    if op == "restar":
        return str(a - b)
    if op == "multiplicar":
        return str(a * b)
    if op == "dividir":
        if b == 0:
            return "error: división por cero"
        return str(int(a / b))  # división entera (truncada)
    return f"error: operación desconocida: {op}"


def clima(inp):
    ciudad = inp.get("ciudad")
    if ciudad in CIUDADES:
        return f"{CIUDADES[ciudad]} °C"
    return f"error: ciudad desconocida: {ciudad}"


HERRAMIENTAS = {"calculadora": calculadora, "clima": clima}


def ejecutar(nombre, inp):
    if nombre in HERRAMIENTAS:
        return HERRAMIENTAS[nombre](inp)
    return f"error: herramienta desconocida: {nombre}"


def main():
    sys.stdin.reconfigure(encoding="utf-8")
    sys.stdout.reconfigure(encoding="utf-8")

    out = []
    llamadas = errores = 0

    for linea in sys.stdin.read().splitlines():
        if not linea.strip():
            continue
        resp = json.loads(linea)
        if resp["stop_reason"] == "tool_use":
            for bloque in resp["content"]:
                if bloque["type"] == "tool_use":
                    res = ejecutar(bloque["name"], bloque["input"])
                    llamadas += 1
                    if res.startswith("error:"):
                        errores += 1
                    out.append(f"tool_result {bloque['id']} {res}")
        elif resp["stop_reason"] == "end_turn":
            texto = "".join(b["text"] for b in resp["content"] if b["type"] == "text")
            out.append(f"final: {texto}")

    out.append(f"resumen: {llamadas} llamadas, {errores} errores")
    print("\n".join(out))


main()