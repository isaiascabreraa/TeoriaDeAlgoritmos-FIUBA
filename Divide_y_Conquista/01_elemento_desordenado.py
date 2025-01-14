
def busqueda_elemento_desordenado(arr, inicio, fin):
    if inicio > fin:
        return None
    
    mitad = (inicio + fin) // 2
        
    if mitad > 0 and arr[mitad] < arr[mitad-1]:
            return arr[mitad-1]
    
    if mitad < len(arr)-1 and arr[mitad] > arr[mitad + 1]:
        return arr[mitad]
    
    valor_buscado = busqueda_elemento_desordenado(arr, mitad + 1, fin)
    if not valor_buscado:
        valor_buscado = busqueda_elemento_desordenado(arr, inicio, mitad - 1)

    return valor_buscado

def elemento_desordenado(arr):
    return busqueda_elemento_desordenado(arr, 0, len(arr) - 1)


def main():
    arr = [0,1,2,3,4,5,8,11,15,13,16,18]
    elemento_encontrado = elemento_desordenado(arr)
    print(f"Elemento: {elemento_encontrado}")

if __name__ == "__main__":
    main()
