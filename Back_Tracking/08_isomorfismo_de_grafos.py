

"""
Problema 07:
Implementar un algoritmo de backtracking que, dados dos grafos, determine si existe un Isomorfismo entre ambos.

Resolucion: ...

La complejidad algoritmica es del orden de: ...
"""

def bt_hay_isomorfismo(g1, g2):
    return False


def hay_isomorfismo(g1, g2):
    return bt_hay_isomorfismo(g1, g2)


def main():

    g1 = []
    g2 = []

    if hay_isomorfismo(g1, g2):
        print(f"Los grafos son isomorfos!")
    else:
        print(f"No hay isomorfismo de grafos")
 
if __name__ == "__main__":
    main()