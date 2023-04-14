""" 
En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt, 
lo abráis y escribáis dentro del archivo. Para ello,
tendréis que acceder dos veces al archivo creado. """


 

fo = open('archivo.txt', 'w')
fo.write('¡Archivo creado!\n')
fo.close()

fo = open('archivo.txt', 'r+')
fo.readline()
fo.write('Accediendo por segunda vez modo  r+.\n')
fo.close()