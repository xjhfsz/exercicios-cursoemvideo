from math import trunc

number = float(input('Digite um valor decimal: '))

print('-' * 15)
print(f'Valor digitado: {number} / Valor inteiro: {trunc(number)}')  # método math.trunc()
print(f'Valor digitado: {number} / Valor inteiro: {int(number)}')  # método int()

