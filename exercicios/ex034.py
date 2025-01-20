salary = float(input('Digite o salário do funcionário: R$ '))

if salary > 1250:
    new_salary = salary + ((salary * 10) / 100)
else:
    new_salary = salary + ((salary * 15) / 100)

print('-' * 20)
print('Calculando aumento de salário...')
print(f'Um funcionário que recebia R$ {salary:.2f}, passa a receber R$ {new_salary:.2f}')