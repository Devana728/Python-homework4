#Даны два файла, в каждом из которых находится запись
#  многочлена. Задача - сформировать файл, содержащий
#  сумму многочленов. 2*x² + 4*x + 5 3*x² +10*x + 6 
# Вывод: 5*x² + 14*x + 11
from random import randint
import itertools

k = randint(2, 7)

def get_ratios(k):
    ratios = [randint(0, 10) for i in range (k + 1)]
    while ratios[0] == 0:
        ratios[0] = randint(1, 10) 
    return ratios

def get_polynomial(k, ratios):
    var = ['*x^']*(k-1) + ['*x']
    polynomial = [[a, b, c] for a, b, c  in itertools.zip_longest(ratios, var, range(k, 1, -1), fillvalue = '') if a !=0]
    for x in polynomial:
        x.append(' + ')
    polynomial = list(itertools.chain(*polynomial))
    polynomial[-1] = ' = 0'
    return "".join(map(str, polynomial)).replace(' 1*x',' x')


ratios = get_ratios(k)
polynom1 = get_polynomial(k, ratios)
print(polynom1)

with open('Polinom.txt', 'w') as data:
    data.write(polynom1)



k = randint(2, 5)

ratios = get_ratios(k) 
polynom2 = get_polynomial(k, ratios)
print(polynom2)

with open('Polinom2.txt', 'w') as data:
    data.write(polynom2)

sum = polynom1 + polynom2
with open('Polinomsum.txt', 'w') as data:
 
    data.writelines(sum) 
data.close()   
