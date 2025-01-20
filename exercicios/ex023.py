number = int(input('Digite um número com até 4 dígitos: '))

unit = number // 1 % 10  # unidade
ten = number // 10 % 10  # dezena
hundred = number // 100 % 10  # centena
thousand = number // 1000 % 10  # milhar


print('-' * 20)
print(f'Analisando o número #{number}')
print(f'Unidade: {unit}')
print(f'Dezena: {ten}')
print(f'Centena: {hundred}')
print(f'Milhar: {thousand}')