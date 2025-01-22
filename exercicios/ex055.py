major = 0
minor = 0

for person in range(1, 6):
    weight = float(input(f'Peso da {person}ª pessoa: '))
    
    if person == 1:  # se for a primeira pessoa
        major = weight
        minor = weight
    else:
        if weight > major:  # se for maior que o maior
            major = weight
        if weight < minor:  # se for menor que o menor
            minor = weight
            
            
print(f'O maior peso lido foi de {major} kg')
print(f'O menor peso lido foi de {minor} kg')