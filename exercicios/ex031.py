distance = int(input('Digite a distância em km: '))

if distance <= 200:
    price = distance * 0.5
else:
    price = distance * 0.45
    
# método alternativo    
# price - distance * 0.50 if distance <= 200 else distance * 0.45

print('-' * 50)
print('Calculando o preço da passagem...')

print(f'O valor da passagem é R$ {price:.2f}')