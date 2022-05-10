def busqueda (lista, key):
  for i in range(len(lista)):
    if lista[i] == key:
      return ("El key " + str(key) + " se encuentra en el indice: " + str(i))
  return ("El key "+ str(key)+ " no se encuentra en la lista")