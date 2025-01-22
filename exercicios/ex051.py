first_item = int(input('Digite o primeiro termo: '))

ratio = int(input('Digite a razão: '))

tenth = first_item + (10 - 1) * ratio  # décimo item da PA

for i in range(
    first_item,  # incício da PA
    tenth + ratio,  # fim da PA (10° item)
    ratio,  # razão
):
    
    print(first_item, end=' -> ')
    first_item += ratio
    
print('FIM!')