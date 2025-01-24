sex = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]

while sex not in 'MF':
    sex = str(input('Dados inválidos. Informe seu sexo: [M/F] ')).strip().upper()[0]

print(f'Sexo {sex} registrado com sucesso!')