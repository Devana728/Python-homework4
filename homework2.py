#Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.
n = int(input('задайте натуральное число N : '))
mass = []
i=2
while n !=1 or i < n:
    if n % i == 0:
        mass.append(i)
        n = n/i
        i = 2
    else:
        i = i+1
print(mass)

