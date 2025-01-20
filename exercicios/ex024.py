city = str(input('Digite o nome da cidade: ')).strip()

# analisa se a string começa com SANTO
result = 'SANTO' == city[:5].upper()

print('-' * 20)
print('Analisando a cidade...')
print(f'Sua cidade começa com Santo? {result}')