print('Sequência de Fibonacci')
print('-' * 20)

terms = int(input('Quantos termos você quer mostrar? '))

term_1 = 0
term_2 = 1

print('~' * 20)
print(f'{term_1} -> {term_2}', end='')

counter = 3

while counter <= terms:
    term_3 = term_1 + term_2
    print(f' -> {term_3}', end='')

    term_1 = term_2
    term_2 = term_3
    
    counter += 1

print(' -- FIM')