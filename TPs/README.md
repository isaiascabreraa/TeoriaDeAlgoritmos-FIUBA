# tda-tp-asinc
Este repositorio contiene la solucion al trabajo practico del curso asincronico de TDA

# Ejecución

Para ejecutar el programa se utiliza el siguiente comando:

```
python3 main.py <algorithm> <path>
```
Donde:
- `<algorithm>` es el algoritmo seleccionado para utilizar, y puede ser:
    - `gr`: Greedy
    - `pd`: Programacion Dinamica
    - `bt`: Backtracking
    - `aprox`: Aproximación
- `<path>` es la dirección de un archivo de datos de entrada para el cual correr el algoritmo, por ejemplo `5.txt` o `100.txt` para los juegos que incluyan monedas o `3_3_2.txt` o `10_10_10.txt` para los que incluyan barcos.
- Si se quiere probar un archivo de datos propio, `<path>` debe ser la ruta del archivo desde el directorio raiz, por ejemplo: /home/user/carpeta_ejemplo/mi_archivo.txt

<br>

# Gráfico de complejidad

Para ver el grafico de complejidad de un algoritmo:

```
Python3 generador_graficos.py <algoritmo>
```
Donde:
- `<algorithm>` puede ser:
  - `gr`: Greedy
  - `pd`: Programacion Dinamica
  - `bt`: Backtracking
  - `aprox`: Aproximación
