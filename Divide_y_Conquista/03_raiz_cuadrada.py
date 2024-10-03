
def busqueda_parte_entera(raiz_buscada, minimo_actual, maximo_actual):
    if minimo_actual+1 >= maximo_actual:
        return minimo_actual

    numero_encontrado = (minimo_actual+maximo_actual) // 2
    valor_obtenido = numero_encontrado*numero_encontrado

    if valor_obtenido > raiz_buscada:
        return busqueda_parte_entera(raiz_buscada, minimo_actual, numero_encontrado)

    elif valor_obtenido < raiz_buscada:
        return busqueda_parte_entera(raiz_buscada, numero_encontrado, maximo_actual)
       
    else:
        return numero_encontrado

def parte_entera_raiz(n):
    if n == 1:
        return 1
    return busqueda_parte_entera(n, 0, n)

def main():
    
    numero = 1
    raiz_encontrada = parte_entera_raiz(numero)
    print(f"Raiz de {numero} es {raiz_encontrada}")

if __name__ == "__main__":
    main()