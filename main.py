import random
#1
A = [1-x for x in range(1,11)]
print(A)
B = [4**x for x in range(8)]
print(B)
C = [x for x in B if x % 2 == 0]
print(C)
#2
listy1=random.sample(range(1,999999999999999999),10)
lista = [x for x in listy1 if x % 2 == 0]
print(lista)
#3
slownik = {'woda':'litry','maka':'kg','banan':'sztuki','cukier':'kg','sol':'kg','sok':'litry','piwo':'litry','wodka':'litry','jajko':'sztuki'}
lista2 = [x for x in slownik if slownik[x] == 'sztuki']
print(lista2)
#4
def trojkat(a,b,c):
    x = max(a,b,c)
    if a**2 + b**2 + c**2 - x**2 == x**2:
        print('trojkat jest kwadratowy')
    else:
        print('trojkat nie jest kwadratowy')
trojkat(1,2,3)
#5
def trapez(a,b,h):
    print(((a+b)*h)/2)
trapez(1,2,3)
#6
def iloczyn(a = 1,b = 4,ile = 10):
    for i in range(ile):
        print(a)
        a=a*b

iloczyn()
#7
def iloczyn2(* ile):
    a=1
    for i in ile:
        print(a)
        a=a*4
iloczyn2(1,2,3,4,5,6,7,8,9,10)
#8

#9
x= int(input())
try:
    print(math.sqrt(x))