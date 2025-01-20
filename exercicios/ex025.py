name = str(input('Digite seu nome completo: ')).strip()

result = 'SILVA' in name.upper()

print('-' * 20)
print('Analisando seu nome...')
print(f'Seu nome tem Silva? {result}')
