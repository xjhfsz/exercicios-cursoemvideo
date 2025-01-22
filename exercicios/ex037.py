number = int(input('Digite um número inteiro: '))

print(
    '''
    Escolha uma das bases para conversão:
    [ 1 ] converter para binário
    [ 2 ] converter para octal
    [ 3 ] converter para hexadecimal
    '''
)

option = int(input('Escolha uma opção de conversão: '))

if option == 1:
    print(f'{number} convertido para binário é {bin(number)[2:]}')
    
elif option == 2:
    print(f'{number} convertido para octal é {oct(number)[2:]}')
    
elif option == 3:
    print(f'{number} convertido para hexadecimal é {hex(number)[2:]}')
    
else:
    print('Opção inválida! Tente novamente.')