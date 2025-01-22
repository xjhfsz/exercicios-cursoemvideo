
sum_age = 0  # soma das idades

older_age = 0  # masculino mais velho
name_older = ''

woman = 0  # qtd de mulheres jovens

for i in range(1, 5):
    print('-' * 10 + f' {i}ª PESSOA ' + '-' * 10)
    name = str(input('Nome: ')).strip().upper()
    age = int(input('Idade: '))
    sex = str(input('Sexo [M/F]: ')).strip().upper()
    
    sum_age += age
    
    if sex == 'M':
        if age > older_age:
            older_age = age
            name_older = name

    if sex == 'F':
        if age < 20:
            woman += 1
        
mean = sum_age / 4  # média das idades
    

print('-' * 10 + ' ANÁLISE DE DADOS ' + '-' * 10)
print(f'A média de idade das pessoas é de {mean:.1f} anos')
print(f'O homem mais velho tem {older_age} anos e se chama {name_older}')
print(f'No total são {woman} mulheres com menos de 20 anos')