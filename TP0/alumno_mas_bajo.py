
class Alumno:
    def __init__(self, nombre, altura):
        self.nombre = nombre
        self.altura = altura

def indice_mas_bajo(alumnos):
    anterior, siguiente = 0, len(alumnos) - 1
    
    while anterior < siguiente:
        actual = (anterior + siguiente) // 2
        
        if alumnos[actual].altura > alumnos[actual + 1].altura:
            anterior = actual + 1
        else:
            siguiente = actual
    return anterior

def validar_mas_bajo(alumnos, indice):
    return (alumnos[indice].altura < alumnos[indice - 1].altura and alumnos[indice].altura < alumnos[indice + 1].altura)

def main():
    alumnos = [
        Alumno("Joaquin", 1.90), #Posicion 0
        Alumno("Micaela", 1.89),
        Alumno("Mirta", 1.88),
        Alumno("Maximiliano", 1.85),
        Alumno("Hector", 1.81),
        Alumno("Pedro", 1.80),
        Alumno("Gerald", 1.79),
        Alumno("Nicolas", 1.75),
        Alumno("Juan", 1.73),
        Alumno("Isaias", 1.70),
        Alumno("María", 1.68), #Posicion 11
        Alumno("Jonathan", 1.69),
        Alumno("Norma", 1.70),
        Alumno("Abraham", 1.71),
        Alumno("Milagros", 1.72),
        Alumno("Camila", 1.73),
        Alumno("Rodrigo", 1.78),
        Alumno("Agustina", 1.79),
        Alumno("Raquel", 1.80),
        Alumno("Martin", 1.82) #Posicion 20
    ]
    indice = indice_mas_bajo(alumnos)
    if validar_mas_bajo(alumnos, indice):
        print("El alumno encontrado es el menor")
    else:
        print("El alumno encontrado NO es el menor")
    
    alumno_encontrado = alumnos[indice]
    print(f"Nombre: {alumno_encontrado.nombre}, Altura: {alumno_encontrado.altura:.2f} metros")

if __name__ == "__main__":
    main()
