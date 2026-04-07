
# Arboles
alejandro Ramirez - 2250930
david gomez - 2252119

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []  # lista de nodos hijos

class Arbol:
    def __init__(self, raiz=None):
        self.raiz = raiz

    def agregar_hijo(self, nodo_padre, valor_hijo):
        nuevo_hijo = Nodo(valor_hijo)
        nodo_padre.hijos.append(nuevo_hijo)
        return nuevo_hijo

    def peso(self, nodo=None):
        if nodo is None:
            nodo = self.raiz
        if nodo is None:
            return 0
        total = 1
        for hijo in nodo.hijos:
            total += self.peso(hijo)
        return total

    def orden(self, nodo=None):
        if nodo is None:
            nodo = self.raiz
        if nodo is None:
            return 0
        max_hijos = len(nodo.hijos)
        for hijo in nodo.hijos:
            max_hijos = max(max_hijos, self.orden(hijo))
        return max_hijos

    def altura(self, nodo=None):
        if nodo is None:
            nodo = self.raiz
        if nodo is None:
            return 0
        if not nodo.hijos:
            return 1
        alturas = [self.altura(hijo) for hijo in nodo.hijos]
        return 1 + max(alturas)


def menu():
    valor_raiz = input("Ingrese el valor de la raíz: ")
    raiz = Nodo(valor_raiz)
    arbol = Arbol(raiz)
    nodos_creados = {valor_raiz: raiz}

    while True:
        print("\n   MENÚ ")
        print("1. Agregar hijo")
        print("2. Mostrar peso del árbol")
        print("3. Mostrar orden del árbol")
        print("4. Mostrar altura del árbol")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            padre = input("Ingrese el valor del nodo padre: ")
            if padre not in nodos_creados:
                print("Ese nodo padre no existe.")
                continue
            valor_hijo = input("Ingrese el valor del hijo: ")
            nuevo = arbol.agregar_hijo(nodos_creados[padre], valor_hijo)
            nodos_creados[valor_hijo] = nuevo
            print(f"Hijo '{valor_hijo}' agregado al padre '{padre}'.")

        elif opcion == "2":
            print("Peso del árbol:", arbol.peso())

        elif opcion == "3":
            print("Orden del árbol:", arbol.orden())

        elif opcion == "4":
            print("Altura del árbol:", arbol.altura())

        elif opcion == "5":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    menu()