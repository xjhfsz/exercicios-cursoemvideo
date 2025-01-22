
sum = 0
count = 0

for i in range(1, 501, 2):  # 1 até 500 de 2 em 2 (ímpares)
    if i % 3 == 0:
        sum += i  # soma + (soma + i)
        count += 1  # contagem + (contagem + 1)
        
print(f'A soma dos ímpares múltiplos de 3 entre 1 e 500 ({count} valores) é: {sum}')