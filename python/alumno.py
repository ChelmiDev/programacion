""" En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno que tenga como atributos su nombre y su nota
. Deberéis de definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha 
aprobado o no. """


class Alumno:

    def __init__(self, nombre, nota):

        self.nombre = nombre
        self.nota = nota

    def aprobado(self):

        if self.nota >= 10:
            print("aprobado")
        else:
            print("No aprobado")

    def imprimir(self):
        
        print("alumno: {}, nota: {}".format(self.nombre, self.nota))
        self.aprobado()

alumno = Alumno("juan", 10)
alumno1 = Alumno("Ana", 9)

alumno.imprimir()
alumno1.imprimir()
