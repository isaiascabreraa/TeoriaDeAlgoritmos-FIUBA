
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
        
    mid = len(arr) // 2
    izquierda = arr[:mid]
    derecha = arr[mid:]

    izquierda = merge_sort(izquierda)
    derecha = merge_sort(derecha)
    return merge(izquierda, derecha)

def merge(izquierda, derecha):
    resultado = []
    i = 0
    j = 0
    
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    while i < len(izquierda):
        resultado.append(izquierda[i])
        i += 1
    while j < len(derecha):
        resultado.append(derecha[j])
        j += 1
    return resultado

def main():
    arr = [38, 27, 43, 3, 9, 82, 10]
    sorted_arr = merge_sort(arr)
    print(f"{sorted_arr}")

if __name__ == "__main__":
    main()