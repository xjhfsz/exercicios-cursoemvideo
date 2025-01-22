from datetime import date

today = date.today().year

major = 0  # maiores de idade

minor = 0  # menores de idade

for i in range(1, 8):
    birthday = int(input(f'Digite o ano de nascimento da {i}ª pessoa: '))
    age = today - birthday
    if age > 17:
        major += 1
    else:
        minor += 1        

print(
    f'''
    Ao todo temos {major} pessoas maiores de idade.
    E temos {minor} pessoas menores de idade.
    '''
)
