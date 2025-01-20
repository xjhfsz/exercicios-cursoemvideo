name = str(input('Digite seu nome completo: ')).strip().upper()

separated_names = name.split()  # lista de nomes separados

print('-' * 20)
print('Muito prazer em conhecer você!')
print(f'Seu primeiro nome é {separated_names[0]}.')
print(f'Seu ultimo nome é {separated_names[len(separated_names) - 1]}.')
