""" En este ejercicio tendréis que crear un módulo que contenga las operaciones básicas de una calculadora: sumar, restar, multiplicar y dividir.

Este módulo lo importaréis a un archivo python y llamaréis a las funciones creadas. Los resultados tenéis que mostrarlos por consola.
 """
from operaciones import *
 


print( "{} + {} = {}".format(100,50,suma(100,50) ) )
print( "{} - {} = {}".format(100,50,resta(100,50) ) )
print( "{} * {} = {}".format(100,50,multiplicar(100,50) ) ) 
print( "{} / {} = {}".format(100,50,division(100,50) ) )

