salary = float(input('Qual é o salário do funcionário? R$ '))

increase = 15  # aumento de 15%

new_salary = salary + (salary * (increase / 100))

print(f'O funcionário que ganhava R$ {salary:.2f}, com {increase}% de aumento, passa a receber R$ {new_salary:.2f}')
