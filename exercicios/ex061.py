print('Gerador de PA')
print('=' * 10 )

first_term = int(input('Primeiro termo da PA: '))
reason = int(input('Razão da PA: '))

counter = 1

print(f'PA: ', end=' ')
while counter <= 10:
    
    print(f'{first_term} -> ', end='')
    first_term += reason
    counter += 1
    
print('FIM')