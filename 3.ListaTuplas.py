def list_tupla(lista):
    return [(int(max(str(y))), int(min(str(y))), int(max(str(y))) + int(min(str(y)))) for y in lista]

print(list_tupla([1234,5678]))
