
def obtener_indice(arr, actual):
    if actual == 0:
        if arr[actual] == 0:
            return actual
        else:
            return actual+1
    if arr[actual-1] == 0:
        return actual-1
    elif arr[actual] == 0:
        return actual
    else:
        return actual+1
    
def verificar_alrededor(arr, actual, numero):
    if actual == 0:
        return arr[actual] == numero and arr[actual+1] == numero and numero != 0
    return arr[actual-1] == numero and arr[actual+1] == numero

def busqueda_primer_cero(arr, inicio, fin):
    if inicio >= fin:
        return -1

    actual = (inicio+fin) // 2
    
    if verificar_alrededor(arr, actual, 1):
        return busqueda_primer_cero(arr, actual+1, fin)

    elif verificar_alrededor(arr, actual, 0):
        return busqueda_primer_cero(arr, inicio, actual)

    else:
        return obtener_indice(arr, actual)

def indice_primer_cero(arr):
    return busqueda_primer_cero(arr, 0, len(arr)-1)

def main():
    #arr = [1,1,1,1,1,0,0,0,0,0,0,0] #El cero esta en el indice 5
    #arr = [1,1,1,1,1,1,1,1,1,1,1,1] #Todo 1
    arr = [0,0,0,0,0,0,0,0,0,0,0,0] #Todo 0
    indice_buscado = indice_primer_cero(arr)
    
    print(f"Indice: {indice_buscado}")

if __name__ == "__main__":
    main()