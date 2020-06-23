lista = [123,456,789]

def num_entero(lista_usuario):
    expresion =(lambda fun: lambda arg: fun(arg)) (lambda a: [[int(x)*3 for x in y] for y in map(str, a)])(lista_usuario)
    print(expresion)

num_entero(lista)







