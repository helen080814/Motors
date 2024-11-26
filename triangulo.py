print("Programa que realiza el triangulo de pascal")
print("Hecho por: Helen A. Carranza C. ")
print("           Andrea Chamorro H.")
def generar_triangulo_pascal(n):
    triangulo = []
    
    for i in range(n):
        fila = [1] * (i + 1)
        for j in range(1, i):
            fila[j] = triangulo[i-1][j-1] + triangulo[i-1][j]
        triangulo.append(fila)
    for fila in triangulo:
        print(" ".join(map(str, fila)))
        
n = int(input("Ingrese el número de filas para el Triángulo de Pascal: "))
generar_triangulo_pascal(n)
