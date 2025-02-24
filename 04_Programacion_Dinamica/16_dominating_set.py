
"""
Sea G un grafo dirigido “camino” (las aristas son de la forma (Vn, Vn-1)). Cada vertice tiene un valor positivo. Implementar un algoritmo que utilizando programacion dinamica, obtenga el Dominating Set de suma 
minima dentro de un grafo de dichas caracteristicas. Indicar y justificar la complejidad espacial del algoritmo implementado, y si hay una optimizacion que permita consumir menos espacio.
"""

def dominating_set_dinamico(camino):    
    OPT = [0] * (len(camino) + 1)    
    OPT[1] = camino[0]    
    OPT[2] = min(camino[0], camino[1])

    for i in range(3, len(camino) + 1):        
        OPT[i] = min(camino[i - 1] + OPT[i - 2], camino[i - 2] + OPT[i - 3])

    return OPT

def reconstruir_solucion(camino, OPT):    
    n = len(camino)    
    seleccionados = []    
    i = n  

    while i > 2:        
        if OPT[i] == camino[i - 1] + OPT[i - 2]:              
            seleccionados.append(i - 1)            
            i -= 2          
        else:              
            seleccionados.append(i - 2)            
            i -= 3  

    if i == 2:
       seleccionados.append(1 if camino[1] < camino[0] else 0)  
    else:        
        seleccionados.append(0)
  
    return seleccionados[::-1]

def main():
    camino = [1, 20, 30, 1, 50, 2]
    OPT = dominating_set_dinamico(camino)
    seleccionados = reconstruir_solucion(camino, OPT)

    print("Valor óptimo:", OPT[-1])
    print("Nodos seleccionados:", seleccionados)

if __name__ == "__main__":
    main()
