class Nodo():
    def __init__(self, valor, izq=None, der=None):
        self.valor = valor
        self.izq = izq
        self.der = der

def en_orden(arbol):
    if arbol == None:
        return []
    return en_orden(arbol.izq) + [arbol.valor] + en_orden(arbol.der)

def list_list(lista):
    return [[int(y) for y in str(x)] for x in lista]

arbol = Nodo(75, Nodo(65, None, Nodo(70)), Nodo(100))

print(list_list(en_orden(arbol)))