lista_base = [123,456,789]

def ultimo_valor(elemento_lista):
    return list(map(int, str(elemento_lista)))

def return_entero(lista):
    if lista == []:
        return ""
    return "{}{}".format(ultimo_valor(lista[0])[-1] , return_entero(lista[1:]))

print(return_entero(lista_base))
