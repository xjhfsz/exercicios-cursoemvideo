from random import shuffle

# não precisa definir o tipo, input() sempre retorna string
name1 = input('Digite o nome do Primeiro aluno: ')
name2 = input('Digite o nome do Segundo aluno: ')
name3 = input('Digite o nome do Terceiro aluno: ')
name4 = input('Digite o nome do Quarto aluno: ')

list = [name1, name2, name3, name4]  # lista de alunos

shuffle(list)  # embaralha a lista

print('-' * 20)
print(f'Ordem de apresentação dos alunos: {list}')