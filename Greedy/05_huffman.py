
"""
Problema 05: Realiza un seguimiento de aplicar el Algoritmo de Huffman al texto "PARALELAMENTE", indicando el binario resultante de comprimirlo.

Resolucion: Para resolverlo debemos:
1. Para cada letra, contar cuantas veces aparece cada letra.

2. Insertamos todos nuestro elementos en un HEAP minimal.
    Al ser un HEAP, los elemento mas pequeños estan en la cima mientras que los mas pequeños caeran al fondo.

3. Al formar el heap, quito los primeros dos elementos y creo un padre para ellos que contenga a los dos y en el que su valor sea la suma de ambos elementos. Luego agrego este padre al
    heap y hago esto para cada uno de los elementos de mi HEAP hasta haber generado un padre para cada par de elementos.

3. Hago lo mismo pero con los nuevos elementos formados anteriormente y repito el proceso hasta obtener el conjunto de letras que valga la cantidad total de letras.

4. Una vez terminado este grafico, lo que haremos es, para el arbol formado ahora en base a los elementos removidos del heap y los agregados al mismo, tomaremos el camino al nodo a la 
    izquierda del nodo actual como 0 y por el derecho como 1.

5. De esta manera, si quiero representar la A por ejemplo, debo recorrer el arbol para ver con que bits puedo representarlo y asi, siendo que la A aparece 3 veces, solo necesito 2 bits
    para representarla.

Nota: Si la cantidad de letras es impar, a la primera letra removida del heap no le generamos un padre.


Una vez cifrado el codigo, para descifrar este codigo necesitamos el arbol de huffman y realizar el proceso inverso.

Este algoritmo es greedy? Si y mi regla es "Hacer que cueste un caracter mas los caracteres que menos frecuencia acumulen".

"""


def huffman(texto):

    def huffman(texto):
	frecuencias = calcular_frecuencias(texto) #type: ignore
	q = heap_crear() #type: ignore
	for caracter in frecuencia: #type: ignore
		q.encolar( Hoja(caracter, frecuencia) ) #type: ignore
	while q.cantidad() > 1:
		t1 = q.desencolar()
		t2 = q.desencolar()
		q.encolar( Arbol(t1, t2, t1.frecuencia + t2.frecuencia) ) #type: ignore
	return codificar(q.desencolar()) #type: ignore

