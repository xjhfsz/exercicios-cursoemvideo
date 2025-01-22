print('-' * 50)
print('Analisando triângulos v2.0')
print('-' * 50)

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triângulo! ', end='')
    
    if r1 == r2 == r3:
        print('Tipo: Equilátero!')    
    elif r1 != r2 != r3 != r1:
        print('Tipo: Escaleno!')
    else:
        print('Tipo: Isósceles!')
    
else:
    print('Os segmentos acima NÃO podem formar um triângulo!')