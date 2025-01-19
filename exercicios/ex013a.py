price_product = float(input('Digite o preço do produto: R$ '))

while True:
  payment = input('Digite a forma de pagamento (V = à vista ou P = parcelado): ')

  if payment in 'vVpP':
    break
  else:
    print('Forma de pagamento inválida! Tente novamente!')


discount = 10  # à vista tem 10% de desconto
increase = 8  # parcelado aumenta 8% no preço

# preço com desconto
discounted_price = price_product - (price_product * (discount / 100))

# preço com aumento
increased_price = price_product + (price_product * (increase / 100))


if payment in 'vV':
  print('--' * 10)
  print(f'Pagamento à vista, preço do produto com desconto de {discount}%: R$ {discounted_price:.2f}')
elif payment in 'pP':
  print('--' * 10)
  print(f'Pagamento parcelado, preço do produto com aumento de {increase}%: R$ {increased_price:.2f}')

