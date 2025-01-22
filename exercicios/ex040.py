print('Cálculo de Média de Notas')

n1 = float(input('Digite a primeira nota: '))

n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2

print('-' * 30)
print(f'A média entre {n1} e {n2} é igual a {media:.1f}')

if media < 5:
    print('Situação do Aluno: REPROVADO')
elif media >= 7:
    print('Situação do Aluno: APROVADO')
else:
    print('Situação do Aluno: RECUPERAÇÃO')