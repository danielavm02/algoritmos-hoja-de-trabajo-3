def maximo (lista):
    Max = lista[0]
    for i in range (len(lista)):
        if (lista[i]> Max):
            Max = lista[i]
    print("El valor máximo de la lista es: " +str(Max)) 