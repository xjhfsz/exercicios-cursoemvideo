print('-' * 20 + ' ANÁLISE DE NÚMEROS PRIMOS ' + '-' * 20)
number = int(input('Digite um número inteiro: '))

count = 0

for i in range(1, number + 1):
    
    if number % i == 0:  # se for divisível
        count += 1  # contagem + (contagem + 1)
        print('\033[32m', end='')
    else:
        print('\033[31m', end='')
    
    print(f'{i} ', end='')
    
print(f'\n\033[mO número {number} foi divisível {count} vezes.')

if count == 2:
    print(f'Portanto, o número {number} é PRIMO!')
else:
    print(f'Portanto, o número {number} NÃO é PRIMO!')