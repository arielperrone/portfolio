profundidad = int(input("ingrese la profundidad del pozo: "))
sube = 7
baja = 2
dia = 0
recorrido = 0

while recorrido < profundidad:
    recorrido = recorrido + sube
    if recorrido >= profundidad:
        print("El caracol tardará ", dia,  "dias en subir")
        break

    else:
        recorrido = recorrido - baja
        dia = dia + 1 

