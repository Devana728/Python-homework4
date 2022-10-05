#Задайте последовательность чисел. Напишите программу,
#  которая выведет список неповторяющихся элементов 
# исходной последовательности.
from random import randint
N = int(input("Введите число N: "))
mass = []

for i in range(N):
    mass.append(randint(0, N))
print(mass)
mass2 = []
for i in mass:
    if mass.count(i)==1:
        mass2.append(i)
print(mass2)
