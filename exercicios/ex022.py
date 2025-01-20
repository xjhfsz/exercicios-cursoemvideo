name = str(input('Digite seu nome completo: ')).strip()

print('-' * 20)
print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é {name.upper()}')
print(f'Seu nome em minúsculas é {name.lower()}')
print(f'Seu nome tem ao todo {len(name) - name.count(" ")} letras')
print(f'Seu primeiro nome tem {name.find(" ")} letras')

separate = name.split()  # separa o nome
print(f'Seu primeiro nome é {separate[0]} e ele tem {len(separate[0])} letras')