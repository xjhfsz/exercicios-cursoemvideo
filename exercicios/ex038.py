print('Comparando números...')
number1 = int(input('Digite um número: '))
number2 = int(input('Digite outro número: '))

if number1 > number2:
    print(f'O primeiro número é maior que o segundo!')
elif number2 > number1:
    print(f'O segundo número é maior que o primeiro!')
else:
    print(f'Os dois números sao iguais!')