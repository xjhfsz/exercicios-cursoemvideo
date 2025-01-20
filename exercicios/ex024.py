city = str(input('Digite o nome da cidade: ')).strip()
result = city[:5].upper() == 'SANTO'

print('-' * 20)
print('Analisando a cidade...')
print(f'Sua cidade começa com Santo? {result}')