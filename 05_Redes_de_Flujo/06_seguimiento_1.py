
def obtener_flujo():
    flujo = {}
    vertices = "super_fuente", "S", "T", "U", "V", "W", "X", "Z"
    flujo[("super_fuente", "S")] = 7
    flujo[("super_fuente", "X")] = 2
    flujo[("S", "V")] = 4
    flujo[("S", "U")] = 3
    flujo[("V", "T")] = 3
    flujo[("V", "W")] = 1
    flujo[("W", "T")] = 6
    flujo[("U", "W")] = 4
    flujo[("X", "Z")] = 2
    flujo[("Z", "W")] = 1
    flujo[("Z", "U")] = 1
    flujo[("U", "Z")] = 0

    conjunto_super_fuente = ['super_fuente', 'S', 'U', 'V', 'W', 'X', 'Z']
    conjunto_sumidero = ['T']

    return flujo, conjunto_super_fuente, conjunto_sumidero

def main():

    flujo, conjunto_super_fuente, conjunto_sumidero = obtener_flujo()

    print(f"{flujo}")
    print(f"Superfuente: {conjunto_super_fuente}")
    print(f"Sumidero: {conjunto_sumidero}")

if __name__ == "__main__":
    main()
