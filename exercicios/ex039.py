from datetime import date

print('Alistamento Militar')

birthday = int(input('Digite o ano do seu nascimento com 4 dígitos: '))

age = date.today().year - birthday

print('-' * 20)
print('Analisando seu alistamento...')

if age == 18:
    print(f'Você completará 18 anos neste ano ({date.today().year}) e deve se alistar IMEDIATAMENTE!')

elif age < 18:
    remain = 18 - age
    print(f'Você ainda é menor de idade ({age} anos) e deve se alistar em {birthday + 18}, faltam {remain} anos.')
    
else:
    remain = age - 18
    print(f'Você completa {age} anos neste ano e já deveria ter se alistado em {birthday + 18}, {remain} anos atrás.')