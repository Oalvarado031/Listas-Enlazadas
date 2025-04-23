# Ejemplificando la creación de una lista enlazada simple con funcionalidades extendidas

# Clase Nodo - representa un nodo de la lista
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

# Clase ListaEnlazada - gestiona la lista y sus operaciones
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    # Insertar un nuevo valor al final de la lista
    def insertar(self, valor):
        nuevo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

    # Insertar un nuevo valor al inicio de la lista
    def insertar_inicio(self, valor):
        nuevo = Nodo(valor)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    # Eliminar el primer nodo que contenga el valor
    def eliminar(self, valor):
        actual = self.cabeza
        anterior = None

        while actual:
            if actual.valor == valor:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                return True  # Valor eliminado
            anterior = actual
            actual = actual.siguiente

        return False  # Valor no encontrado

    # Método para buscar un valor en la lista
    def buscar(self, valor):
        actual = self.cabeza
        while actual:
            if actual.valor == valor:
                return True
            actual = actual.siguiente
        return False

    # Método que imprime los valores de la lista
    def imprimir(self):
        actual = self.cabeza
        if not actual:
            print("La lista está vacía")
            return
        print("Lista enlazada:", end=" ")
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")

    # Método que cuenta los nodos de la lista
    def longitudLista(self):
        contador = 0
        actual = self.cabeza
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador

    # Método para determinar si la lista está vacía
    def estaVacia(self):
        return self.cabeza is None

    # Método que imprime el último valor de la lista
    def mostrarUltimo(self):
        if not self.cabeza:
            print("La lista está vacía")
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            print("Último valor de la lista:", actual.valor)


if __name__ == "__main__":
    lista = ListaEnlazada()  # Creando el objeto lista

    # Leer datos para insertar al final
    entrada = input("Ingrese los valores a insertar al final, separados por espacios: ")
    for val in entrada.split():
        lista.insertar(val)

    lista.imprimir()

    # Demostración de inserción al inicio
    valor_inicio = input("Ingrese un valor para insertar al inicio: ")
    lista.insertar_inicio(valor_inicio)
    lista.imprimir()

    # Mostrar longitud de la lista
    print("Longitud de la lista:", lista.longitudLista())

    # Verificar si la lista está vacía
    print("¿La lista está vacía?", lista.estaVacia())

    # Mostrar el último valor de la lista
    lista.mostrarUltimo()
