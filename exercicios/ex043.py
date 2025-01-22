print('Calculando Índice de Massa Corporal (IMC)')

# peso
weight = float(input('Digite o peso em kg: '))

# altura
height = float(input('Digite a altura em metros: '))

imc = weight / (height * height)

print('-' * 50)
print(f'IMC: {imc:.1f} > ', end='')

if imc < 18.5:
    print('Abaixo do peso!')

elif imc < 25:
    print('Peso ideal!')

elif imc < 30:
    print('Sobrepeso!')

elif imc < 40:
    print('Obesidade!')

else:
    print('Obesidade mórbida!')