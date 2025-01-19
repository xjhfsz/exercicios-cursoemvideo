# para cada 2m² de parede, necessário 1 litro de tinta

height = float(input('Altura da parede (metros): '))  # altura
width = float(input('Largura da parede (metros): '))  # largura

area = height * width  # área da parede

paint = area / 2  # quantidade de tinta necessária

print('*' * 30)
print(f'Dimensão da parede: {height} x {width} m')
print(f'Área da parede: {area:.2f} m²')
print(f'Quantidade de tinta necessária: {paint:.2f} litros')

