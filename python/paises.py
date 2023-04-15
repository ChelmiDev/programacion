items = input("Introduce países separados por comas:\n")
paises=[]
for pais in items.split(","):
    paises.append(pais)

resultado = ",".join(sorted(set(paises)))

print(resultado)

