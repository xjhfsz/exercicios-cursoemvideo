print('Simulação de Financiamento')

value = float(input('Qual o valor da casa? R$ '))

salary = float(input('Qual o seu salario? R$ '))

max = salary * 0.3  # valor máximo da parcela

years = int(input('Em quantos anos pretende pagar? '))

quota = value / (years * 12)  # valor máximo da parcela

print('-' * 30)
print('Analisando o financiamento...')
print(f'Para pagar uma casa de R$ {value:.2f} em {years} anos, a prestação será de R$ {quota:.2f}')

if quota > max:  # se parcela for maior de 30% do salário
    print('Financiamento negado! Valor da parcela maior que 30% do seu salario.')
else:
    print(f'Financiamento aprovado! Valor da parcela menor que 30% do seu salario.')
