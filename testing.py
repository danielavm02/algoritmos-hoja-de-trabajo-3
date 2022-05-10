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

A=[1,3,5,7,9]
B=[2,4,6,8,10]
# maximo.maximo(A)
# print(list_merge.juntar(A,B))
# sum_numbers.suma(5)
# print(pin_unlock.unlock("2812"))
# print(" Divisores: " + str(divisores_n.divisores(9)))
# print(sum_of_n.sum(30))
# print(fibonacci.fibonacci(10))
#print (factorial.fact(5))
# countdown.cuenta(10)
list=[4,1,9,8,6,10]
# print(bubble_sort.bubble_sort(list))
print(selection_sort.selection_sort(list))
print(bubble_opt.bubble_sort_opt(list))