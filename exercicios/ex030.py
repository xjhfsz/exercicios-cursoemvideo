# crie um programa que diga se um número é par ou ímpar

number = int(input('Digite um número: '))

result = number % 2

print('-' * 20)
print('Analisando se o número...')
if number == 0:
    print('Número ZERO!')  # se for zero
elif result == 0:
    print(f'O número {number} é par!')  # se for par
else:
    print(f'O número {number} é ímpar!')  # se for ímpar