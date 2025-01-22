sum = 0  # soma dos números pares
count = 0

for i in range(0, 6):
    n = int(input(f'Digite um número inteiro: '))
    
    if n % 2 == 0:
        sum += n  # soma + (soma + i)
        count += 1  # contagem + (contagem + 1)
    
        
print('-' * 20)        
print(f'Quantidade de números pares: {count}')
print(f'Soma dos números pares: {sum}')