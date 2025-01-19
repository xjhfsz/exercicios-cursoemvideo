from math import hypot


opposite_leg = float(input('Comprimento do cateto oposto: '))
adjacent_leg = float(input('Comprimento do cateto adjacente: '))

# hypotenuse = (opposite_leg ** 2 + adjacent_leg ** 2) ** 0.5  # python puro

hypotenuse = hypot(opposite_leg, adjacent_leg)  # método math.hypot()

print(f'A hipotenusa do triângulo retângulo é {hypotenuse:.2f}')
