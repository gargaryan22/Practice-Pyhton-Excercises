from random import randint

def smaller_elements(arg):
    return [i for i in Salaries if i < arg]


Salaries = [randint(1, 20)*100000 for i in range(1, 11)]

salary = int(input('Enter the salary amount\n'))

print(smaller_elements(salary))

print(Salaries)