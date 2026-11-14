# Hackathon Tests

# Autora: Ángela Gómez

**Nota**: Debido a la complejidad de algunos ejercicios, el código fue retroalimentado por Claude (hace mucho no programo en Python para este tipo de ejercicios)

## Cómo ejecutar cualquier ejercicio

```bash
cd google/A_d1000000
python answer.py < my_input.txt > my_output.txt   # el input dado por los html
```
```bash
cd anthropic/A_streaming
python answer.py < my_input.txt > my_output.txt   # el input dado por los html
```
---

# Parte 1: Prueba Google (Code Jam)

Resumen de los cinco ejercicios:

| Ejercicio | Tema | Técnica principal | Estructura de datos | Complejidad |
|---|---|---|---|---|
| A. d1000000 | Ordenamiento y voraz | Ordenar + greedy | Lista ordenada | O(N log N) |
| B. Moons and Umbrellas | Programación dinámica | DP con 2 estados | 2 variables (`dc`, `dj`) | O(N) |
| C. Parenting Partnering Returns | Intervalos y voraz | Ordenar por inicio + greedy | Lista de tuplas, 2 "relojes" | O(N log N) |
| D. Chain Reactions | Árboles / DFS | Recorrido bottom-up en bosque | Lista de hijos, arreglo `mejor` | O(N) |
| E. Bathroom Stalls | Eficiencia con números enormes | Conteo de segmentos por tamaño | Diccionario `tamaño -> cantidad` | O(log N) |

---

## A. d1000000 (Ordenamiento y voraz)

**Problema.** Dados N dados con `S_i` caras, formar la escalera 1, 2, 3, ..., L usando cada dado a lo sumo una vez. Se pide el mayor L.

**Algoritmo: ordenar + greedy.**
1. Ordenar los dados de menor a mayor número de caras.
2. Mantener `largo` (longitud actual de la escalera).
3. Para cada dado: si `S_i > largo`, el dado puede mostrar `largo + 1`, entonces `largo += 1`. Si no, se descarta.

**Por qué funciona (argumento voraz).** Procesar los dados pequeños primero evita "desperdiciar" dados grandes en valores bajos. Si un dado no alcanza el siguiente valor necesario (`S_i <= largo`), tampoco serviría para valores mayores, así que descartarlo es seguro.

---

## B. Moons and Umbrellas (Programación dinámica)

**Problema.** Dada una cadena de `C`, `J` y `?`, reemplazar cada `?` para minimizar el costo total: cada `CJ` cuesta X y cada `JC` cuesta Y (pueden ser negativos).

**Algoritmo: programación dinámica con dos estados por posición.**

- `dc[i]` = costo mínimo de la subcadena hasta `i` si la letra en `i` es C.
- `dj[i]` = costo mínimo de la subcadena hasta `i` si la letra en `i` es J.

**Recurrencia:**

```
dc[i] = min(dc[i-1], dj[i-1] + Y)     si s[i] != 'J'   (si no, INF)
dj[i] = min(dj[i-1], dc[i-1] + X)     si s[i] != 'C'   (si no, INF)
```

**Caso base:** `dc[0] = 0` si `s[0] != 'J'`; `dj[0] = 0` si `s[0] != 'C'` (el estado inválido vale INF).

**Respuesta:** `min(dc[n-1], dj[n-1])`.

---

## C. Parenting Partnering Returns (Intervalos y voraz)

**Problema.** Asignar N actividades `[s, e)` a Cameron (C) y Jamie (J) sin que ninguno tenga dos actividades simultáneas, o decir `IMPOSSIBLE`.

**Algoritmo: ordenar por inicio + greedy con dos "relojes".**
1. Guardar cada actividad como `(inicio, fin, índice_original)` y ordenar por inicio.
2. Mantener `fin_C` y `fin_J` (momento en que cada persona queda libre, inicialmente 0).
3. Para cada actividad: si `fin_C <= inicio` se asigna a C; si no, si `fin_J <= inicio` se asigna a J; si ninguno está libre, el caso es `IMPOSSIBLE`.
4. Reconstruir la cadena en el **orden original** usando el índice guardado.

**Por qué funciona.** Si en algún instante hay tres actividades solapadas, ninguna asignación sirve. Si nunca hay tres solapadas, procesar por inicio con cualquier persona libre es suficiente (grafo de intervalos 2-coloreable). La condición es `<=` porque una actividad puede comenzar justo cuando otra termina.

---

## D. Chain Reactions (Árboles y DFS)

**Problema.** N módulos con diversión `F_i`; cada módulo apunta a un `P_i < i` o al abismo (0). Los módulos a los que nadie apunta son iniciadores; activar uno recorre su cadena y aporta el mayor F de lo que activó. Maximizar la diversión total escogiendo el orden de los iniciadores.

**Modelo:** los punteros forman un **bosque** (varios árboles cuya raíz virtual es el abismo 0). Los iniciadores son las hojas.

**Algoritmo: recorrido bottom-up (hijos antes que padres).** Como `P_i < i`, recorrer `i = N ... 1` ya garantiza que todos los hijos de `i` se procesan antes que `i`; no hace falta recursión.

**Recurrencia.** Sea `mejor[i]` el valor de la cadena que "sube" por el nodo `i`:

```
si i es hoja:          mejor[i] = F[i]
si no:                 m = min(mejor[k] para k hijo de i)
                       total += sum(mejor[k]) - m
                       mejor[i] = max(F[i], m)
```

**Idea.** Entre las cadenas de los hijos, solo una puede continuar pasando por `i`. Conviene que sea la de **menor** valor, porque las demás se cierran antes de llegar a `i` y aportan su valor completo. Para los hijos de la raíz virtual 0, todas las cadenas se cierran y se suman completas.

---

## E. Bathroom Stalls (Eficiencia con números enormes)

**Problema.** N cubículos (hasta 10^18) y K personas que eligen según una regla. Hallar `max(L, R)` y `min(L, R)` de la última persona.

**Observación clave.** Cada vez que alguien ocupa un segmento libre de tamaño `x`, lo parte en dos segmentos de tamaño `x // 2` y `(x - 1) // 2`. En cada "nivel" solo existen **como máximo dos tamaños distintos** (consecutivos), así que no hace falta simular persona por persona.


---

## Algunas evidencias del ejercicio


---

# Parte 2: Prueba Anthropic (API de Claude)

> Sección preparada.

Resumen de los cinco ejercicios:

| Ejercicio | Tema | Técnica principal | Estructura de datos | Complejidad |
|---|---|---|---|---|
| A. Respuesta en streaming | Streaming (eventos SSE) | Máquina de estados sobre eventos | _pendiente_ | _pendiente_ |
| B. Uso de herramientas | Tool use | Despachador de herramientas | _pendiente_ | _pendiente_ |
| C. Costos con caché | Prompt caching y precios | Aritmética entera en millonésimas de dólar | _pendiente_ | _pendiente_ |
| D. Límites de velocidad | Rate limits | Cubeta de tokens (token bucket) | _pendiente_ | _pendiente_ |
| E. Evaluación de respuestas | Evals calificadas con código | Normalización + coincidencia de palabras completas | _pendiente_ | _pendiente_ |

---

## A. Respuesta en streaming

**Problema.** Reconstruir mensajes completos a partir de eventos `event:` / `data:` (streaming) e imprimir `texto`, `stop_reason`, `input_tokens` y `output_tokens` al llegar `message_stop`.

**Algoritmo / técnica:** _pendiente_ (procesar los eventos en orden; `message_start` da `input_tokens`, cada `content_block_delta` con `text_delta` agrega texto al bloque de su `index`, `message_delta` da `stop_reason` y `output_tokens`, `ping` se ignora).

**Estructura de datos:** _pendiente_ (por ejemplo, un diccionario `index -> texto` para unir los bloques en orden).

**Complejidad:** _pendiente_.

**Evidencias:**
![Ejemplo A Anthropic](img/anthropic_A_ejemplo.png)
![Entrada oficial A Anthropic](img/anthropic_A_oficial.png)

---

## B. Uso de herramientas

**Problema.** Por cada respuesta con `stop_reason: tool_use`, ejecutar las herramientas pedidas (`calculadora`, `clima`) en orden e imprimir `tool_result <id> <resultado>`; con `end_turn` imprimir `final:` y el resumen de llamadas y errores.

**Algoritmo / técnica:** _pendiente_ (despacho por nombre de herramienta y manejo de errores).

**Estructura de datos:** _pendiente_ (por ejemplo, diccionario de ciudades y temperaturas, contadores de llamadas y errores).

**Complejidad:** _pendiente_.

**Evidencias:**
![Ejemplo B Anthropic](img/anthropic_B_ejemplo.png)
![Entrada oficial B Anthropic](img/anthropic_B_oficial.png)

---

## C. Costos con caché de prompts

**Problema.** Calcular el costo de cada llamada con precios de ejemplo ($3 por millón de entrada, $15 por millón de salida, escritura en caché 1,25x y lectura 0,1x), y el total, el costo sin caché, el ahorro y los aciertos de caché.

**Algoritmo / técnica:** _pendiente_ (aritmética con enteros en millonésimas de dólar para evitar errores de redondeo con flotantes).

**Estructura de datos:** _pendiente_.

**Complejidad:** _pendiente_.

**Evidencias:**
![Ejemplo C Anthropic](img/anthropic_C_ejemplo.png)
![Entrada oficial C Anthropic](img/anthropic_C_oficial.png)

---

## D. Límites de velocidad

**Problema.** Simular una cubeta de tokens para solicitudes (capacidad 3, recarga 1/s) y tokens de entrada (capacidad 100, recarga 20/s), respondiendo `ok` o `429 retry-after=N`. Los tokens leídos de caché no cuentan.

**Algoritmo / técnica:** _pendiente_ (token bucket con recarga proporcional al tiempo transcurrido y espera calculada con redondeo hacia arriba).

**Estructura de datos:** _pendiente_ (estado de ambas cubetas y la última marca de tiempo).

**Complejidad:** _pendiente_.

**Evidencias:**
![Ejemplo D Anthropic](img/anthropic_D_ejemplo.png)
![Entrada oficial D Anthropic](img/anthropic_D_oficial.png)

---

## E. Evaluación de respuestas

**Problema.** Normalizar respuesta y esperado (minúsculas, sin tildes, todo lo que no sea letra o número pasa a espacio) y aprobar si lo esperado aparece como palabras completas. Imprimir aprobadas/total por categoría (orden alfabético) y el total con un decimal.

**Algoritmo / técnica:** _pendiente_ (normalización Unicode y búsqueda de subcadena delimitada por espacios).

**Estructura de datos:** _pendiente_ (diccionario de categoría a contadores).

**Complejidad:** _pendiente_.

---