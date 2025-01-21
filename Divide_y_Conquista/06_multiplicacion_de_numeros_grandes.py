
def multiplicar(a, b):
    if a < 10 or b < 10:
        return a * b

    n = max(len(str(a)), len(str(b)))
    m = n // 2

    high_a = a // 10**m
    low_a = a % 10**m
    high_b = b // 10**m
    low_b = b % 10**m

    z0 = multiplicar(low_a, low_b)
    z1 = multiplicar(high_a, high_b)
    z2 = multiplicar(low_a + high_a, low_b + high_b)

    return z1 * 10**(2 * m) + (z2 - z1 - z0) * 10**m + z0

def main():
    resultado = multiplicar(50, 100)
    print(f"{resultado}")

if __name__ == "__main__":
    main()