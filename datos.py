from tabulate import tabulate
database = []
print("Programa que genera una base de datos")
print("Hecho por: CHAMORRO HERNANDEZ ANDREA")
print("           CARRANZA CALVARIO HELEN ABIGAIL")

contraseña = "191997"

def verificar_contraseña():
    intento = input("Ingrese la contraseña: ")
    if intento == contraseña:
        print("Acceso concedido.")
        return True
    else:
        print("Contraseña incorrecta.")
        return False

def agregar_auto():
    print("\n--- Agregar Nuevo Auto ---")
    auto = {
        "Marca": input("Marca: "),
        "Motor": input("Motor: "),
        "Módulo": input("Módulo: "),
        "Estado": input("Estado (Nuevo/Usado): "),
        "Kilometraje": input("Kilometraje: "),
        "Potencia": input("Potencia: "),
        "Precio": input("Precio: "),
        "Color": input("Color: "),
        "No. Serie": input("Número de Serie: "),
        "No. Puertas": input("Número de Puertas: "),
    }
    database.append(auto)
    print("Auto agregado con éxito.")

def consultar_autos():
    print("\n--- Consultar Autos ---")
    if not database:
        print("No hay autos en la base de datos.")
    else: 
      
        headers = list(database[0].keys())  
        table = [list(auto.values()) for auto in database]  
        print(tabulate(table, headers=headers, tablefmt="grid"))

def modificar_auto():
    print("\n--- Modificar Auto ---")
    consultar_autos()
    if database:
        try:
            index = int(input("\nIngrese el número del auto que desea modificar: ")) - 1
            if 0 <= index < len(database):
                print("\nIngrese los nuevos valores (deje en blanco para no modificar):")
                for clave in database[index].keys():
                    nuevo_valor = input(f"{clave} ({database[index][clave]}): ")
                    if nuevo_valor:
                        database[index][clave] = nuevo_valor
                print("Auto modificado con éxito.")
            else:
                print("Número de auto inválido.")
        except ValueError:
            print("Entrada no válida.")

# Función para eliminar un auto
def eliminar_auto():
    print("\n--- Eliminar Auto ---")
    consultar_autos()
    if database:
        try:
            index = int(input("\nIngrese el número del auto que desea eliminar: ")) - 1
            if 0 <= index < len(database):
                eliminado = database.pop(index)
                print(f"El auto {eliminado['Marca']} ha sido eliminado.")
            else:
                print("Número de auto inválido.")
        except ValueError:
            print("Entrada no válida.")

# Menú principal
def menu():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Agregar Auto")
        print("2. Consultar Autos")
        print("3. Modificar Auto")
        print("4. Eliminar Auto")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_auto()
        elif opcion == "2":
            consultar_autos()
        elif opcion == "3":
            modificar_auto()
        elif opcion == "4":
            eliminar_auto()
        elif opcion == "5":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Inicio del programa
print("")
if __name__ == "__main__":
    print("Bienvenido al sistema de gestión de autos.")
    if verificar_contraseña():
        menu()
