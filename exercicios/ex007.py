nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))

media = (nota1 + nota2) / 2

print(f'A média entre {nota1} e {nota2} é igual a {media:.1f}') # método padrão: arredondar

# # método round() do Python: arredondar
# media = round((nota1 + nota2) / 2, 1)  # uma casa decimal
#
# print(f'A média entre {nota1} e {nota2} é igual a {media}')
