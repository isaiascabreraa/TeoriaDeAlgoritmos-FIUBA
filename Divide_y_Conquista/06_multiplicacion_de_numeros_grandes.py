

def multiplicar(a, b):
    if b == 0:
        return 0
    
    return a + multiplicar(a, b - 1)


def main():
    resultado = multiplicar(50,100)
    print(f"{resultado}")

if __name__ == "__main__":
    main()