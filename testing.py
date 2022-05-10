from lists import maximo
from lists import list_merge
from bruteforce import sum_numbers
from bruteforce import pin_unlock
from bruteforce import divisores_n
from recursion import sum_of_n
from recursion import fibonacci
from recursion import factorial
from recursion import countdown
from sorting import bubble_sort
from sorting import selection_sort
from sorting import bubble_opt
from sorting import insertion_sort
from searching import linearsearch
from searching import binarysearch

A=[1,3,5,7,9]
B=[2,4,6,8,10]
print("largest number in list:")
#maximo.maximo(A)
print("list merge:")
#print(list_merge.juntar(A,B))
print("suma de los primeros n numeros:")
#sum_numbers.suma(5)
print("pin unlock:")
#print(pin_unlock.unlock("2812"))
print("divisores de un numero n:")
#print(" Divisores: " + str(divisores_n.divisores(9)))
print("suma de los primeros n numeros con recursion:")
#print(sum_of_n.sum(30))
print ("numero n en la secuencia fibonacci:")
#print(fibonacci.fibonacci(10))
print("factorial del numero n:")
#print (factorial.fact(5))
print("cuenta regresiva:")
#countdown.cuenta(10)
list=[4,1,9,8,6,10]
print ("bubble sort:")
#print(bubble_sort.bubble_sort(list))
print("selection sort:")
#print(selection_sort.selection_sort(list))
print ("bubble sort optimizado:")
#print(bubble_opt.bubble_sort_opt(list))
print("insertion sort:")
#print(insertion_sort.insertion_sort(list))
print ("linear search:")
#print(linearsearch.busqueda(A,5))
print("binary search:")
#print(binarysearch.binary_search(A,5))