from datetime import date

print('Análise de Atletas')

birthday = int(input('Digite o ano de nascimento do atleta: '))

today = date.today().year  # ano atual

age = today - birthday

print('-' * 20)
print(f'Analisando categoria do atleta...')

if age <= 9:
    print(f'Idade do atleta: {age} anos// Classificação: MIRIM')

elif age <= 14:
    print(f'Idade do atleta: {age} anos// Classificação: INFANTIL')

elif age <= 19:
    print(f'Idade do atleta: {age} anos// Classificação: JUNIOR')

elif age <= 25:
    print(f'Idade do atleta: {age} anos// Classificação: SENIOR')

else:
    print(f'Classificação: MASTER')