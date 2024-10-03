
def seleccionar_elemento(arr, actual, final):
    if arr[actual-1] > arr[actual]:
        return actual-1
    elif arr[actual+1] < arr[actual]:
        return actual+1
    else:
        return actual 

def verificar_alrededor(arr, actual, final):
    if actual == 0:
        return arr[actual] < arr[actual+1]
    elif actual == final:
        return arr[actual] > arr[actual-1]
    else:
        return arr[actual] >= arr[actual-1] and arr[actual] < arr[actual+1]

def busqueda_elemento_desordenado(arr, actual, final):
    if actual > final:
        return -1

    if verificar_alrededor(arr, actual, final):
        return busqueda_elemento_desordenado(arr, actual+1, final)
    else:
        return seleccionar_elemento(arr, actual, final)

def elemento_desordenado(arr):
    return arr[busqueda_elemento_desordenado(arr, 0, len(arr) - 1)]

def main():
    arr = [0,1,2,3,4,5,8,11,15,13,16,18]
    elemento_encontrado = elemento_desordenado(arr)
    
    print(f"Elemento: {elemento_encontrado}")

if __name__ == "__main__":
    main()
