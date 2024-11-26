print("Programa que realiza la solucion de la serie de Fibonacci")
print("Hecho por Andrea Chamorro Hernandez")
def solucion(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

n = int(input("Introduce el número de términos: "))
solucion(n)
