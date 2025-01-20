speed_car = int(input('Qual a velocidade do carro? '))

tax = (speed_car - 80) * 7  # valor da multa

print('-' * 20)
if speed_car > 80:
    print('MULTADO! Você excedeu o limite de velocidade de 80 km/h')
    print(f'Você deve pagar uma multa de R$ {tax:.2f}')
else:
    print('Tudo certo! Dirija com segurança!')