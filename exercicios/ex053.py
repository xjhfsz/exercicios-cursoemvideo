print('-' * 20)
print('-' * 20 + ' ANÁLISE DE PALÍNDROMO ' + '-' * 20)

sentence = str(input('Digite uma frase: ')).strip().upper()

words = sentence.split()  # palavras separadas

together = ''.join(words)  # palavras juntas

# MÉTODO 1:
reverse = ''  # letra invertidas
for letter in range(
    len(together) - 1,  # último elemento da lista
    -1,  # até o primeiro elemento da lista
    -1,  # caminha do fim para o começo
):
    
    reverse += together[letter]

# MÉTODO 2
# reverse = together[::-1]

print(f'O reverso de {together} é {reverse}.')

if together == reverse:
    print(f'Portando, a frase "{sentence}" É UM PALÍNDROMO!')
else:
    print(f'Portanto, a frase "{sentence}" NÃO é um Palíndromo!')
