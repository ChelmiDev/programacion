from functools import reduce

def impares(lista):
    
    resultado = list(filter(lambda x: x % 2, lista))
    print(list(resultado))

    
    resultado = reduce(lambda a, b: a + b, resultado)
    print(resultado)
        
lista = list(range(100) )
impares(lista)
 