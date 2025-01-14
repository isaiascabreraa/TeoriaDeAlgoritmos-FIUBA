
def multiplicar(a, b):

    # Caso base: si los números tienen un solo dígito, multiplica directamente
    if a < 10 or b < 10:
        return a * b

    # Calcula la longitud de los números
    n = max(len(str(a)), len(str(b)))
    m = n // 2

    # Divide los números en mitades
    high_a = a // 10**m
    low_a = a % 10**m
    high_b = b // 10**m
    low_b = b % 10**m

    # Conquista: calcula los tres productos recursivamente
    z0 = multiplicar(low_a, low_b)
    z1 = multiplicar(high_a, high_b)
    z2 = multiplicar(low_a + high_a, low_b + high_b)

    # Combina los resultados
    return z1 * 10**(2 * m) + (z2 - z1 - z0) * 10**m + z0

def main():
    resultado = multiplicar(50, 100)
    print(f"{resultado}")

if __name__ == "__main__":
    main()