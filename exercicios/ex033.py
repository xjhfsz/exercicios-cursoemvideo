value1 = int(input('Digite um número: '))
value2 = int(input('Digite outro número: '))
value3 = int(input('Digite outro número: '))


min = value1  # menor valor

if value2 < value1 and value2 < value3:
    min = value2

if value3 < value1 and value3 < value2:
    min = value3

max = value1  # maior valor

if value2 > value1 and value2 > value3:
    max = value2

if value3 > value1 and value3 > value2:
    max = value3

print('-' * 30)
print(f'O menor valor digitado foi {min}!')
print(f'O maior valor digitado foi {max}!')