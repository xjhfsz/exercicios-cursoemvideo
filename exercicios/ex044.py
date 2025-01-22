print('-' * 10 + ' CÁLCULO DE PAGAMENTOS ' + '-' * 10)

price = float(input('Digite o preço total da compra: R$ '))

print(
    '''
    ==== FORMAS DE PAGAMENTO:
    [ 1 ] DINHEIRO 
    [ 2 ] DÉBITO / PIX
    [ 3 ] DÉBITO
    [ 4 ] CRÉDITO PARCELADO
    '''
)

payment_method = int(input('Forma de pagamento: '))

print('-' * 50)
print(f'Valor total da compra: R$ {price:.2f}')

if payment_method == 1:
    new_price = price - (price * 0.1)  # 10% de desconto

    print(f'Desconto: 10%')
    print(f'Valor final: R$ {new_price:.2f}')
    
elif payment_method == 2:
    new_price = price - (price * 0.05)  # 5% de desconto
    print(f'Desconto: 5%')
    print(f'Valor final: R$ {new_price:.2f}')
    
elif payment_method == 3:  # valor normal
    print(f'Desconto: 0%')
    print(f'Valor final: R$ {price:.2f}')
    
elif payment_method == 4:
    print('=== PARCELAMENTO ===')
    new_price = price + (price * 0.2)  # 20% de juros
    parcel = int(input('Divido em quantas parcelas? '))
    price_parcel = new_price / parcel
    
    if 2 <= parcel <= 10:  # 2x até 10x
        print(f'Compra parcelada em {parcel}x com juros de 20%')
        print(f'Valor final: R$ {new_price:.2f}')
        print(f'Valor de cada parcela: R$ {price_parcel:.2f}')
    else:
        print('Quantidade de parcelas inválida! Tente novamente!')
    
else:
    print('Forma de pagamento inválida! Tente novamente!')

print('-' * 20)