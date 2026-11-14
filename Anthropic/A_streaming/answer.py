import sys
import json


def main():
    sys.stdin.reconfigure(encoding="utf-8")
    sys.stdout.reconfigure(encoding="utf-8")

    out = []
    bloques = {}
    entrada = salida = 0
    stop = None

    for linea in sys.stdin.read().splitlines():
        linea = linea.strip()
        if not linea.startswith("data:"):
            continue
        d = json.loads(linea[5:].strip())
        tipo = d.get("type")

        if tipo == "message_start":
            bloques = {}
            stop = None
            entrada = d["message"]["usage"]["input_tokens"]
        elif tipo == "content_block_start":
            bloques.setdefault(d["index"], "")
        elif tipo == "content_block_delta":
            delta = d["delta"]
            if delta.get("type") == "text_delta":
                i = d["index"]
                bloques[i] = bloques.get(i, "") + delta["text"]
        elif tipo == "message_delta":
            stop = d["delta"]["stop_reason"]
            salida = d["usage"]["output_tokens"]
        elif tipo == "message_stop":
            texto = "".join(bloques[i] for i in sorted(bloques))
            out.append(f"texto: {texto}")
            out.append(f"stop_reason: {stop}")
            out.append(f"input_tokens: {entrada}")
            out.append(f"output_tokens: {salida}")
        # ping y los demás eventos se ignoran

    print("\n".join(out))


main()