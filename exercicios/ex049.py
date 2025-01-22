print('-' * 15 + 'TABUADA' + '-' * 15)

number = int(input('Digite um número para ver a tabuada: '))

print('-' * 50)
print(f'Tabuada do {number}')

for i in range(1, 11):
    print(f'{number} x {i:2} = {number * i}')
