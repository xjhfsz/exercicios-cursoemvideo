from random import choice

name1 = input('Digite o nome do Primeiro aluno: ')
name2 = input('Digite o nome do Segundo aluno: ')
name3 = input('Digite o nome do Terceiro aluno: ')
name4 = input('Digite o nome do Quarto aluno: ')

list = [name1, name2, name3, name4]  # lista de alunos

chosen = choice(list)  # aluno escolhido

print('-' * 20)
print(f'Aluno sorteado: {chosen}')