print('Gerador de PA')
print('=' * 10 )

first_term = int(input('Primeiro termo da PA: '))
reason = int(input('Razão da PA: '))

term = first_term

counter = 1
total = 0
more = 10

while more != 0:
    total += more
    while counter <= total:
        print(f'{term} -> ', end='')
        term += reason
        counter += 1
    print('PAUSA')
    more = int(input('Quantos termos você quer mostra a mais? '))
print(f'PA finalizada com {total} termos mostrados.')