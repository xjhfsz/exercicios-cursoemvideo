from math import factorial

number = int(input('Digite um número para calcular seu fatorial: '))
counter = number

print(f'Calculando {number}! = ', end='')

while counter > 0:
    print(f'{counter}', end='')
    print(' x ' if counter > 1 else ' = ', end='')
    counter -= 1

print(f'{factorial(number)}')
print(f'\nO fatorial de {number} é {factorial(number)}')