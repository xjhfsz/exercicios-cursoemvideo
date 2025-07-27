
while True:

    value1 = int(input('Digite o primeiro valor (int):'))
    value2 = int(input('Digite o segundo valor (int):'))

    print(
        f'''
        =======================
        Primeiro valor: {value1}
        Segundo valor: {value2}
        =======================
        Escolha uma opção:
        [ 1 ] Somar valores
        [ 2 ] Multiplicar valores
        [ 3 ] Maior valor
        [ 4 ] Escolher Novos valores
        [ 5 ] Sair do programa
        =======================
        '''
    )

    option = int(input('Opção escolhida: '))

    if option == 1:
        print(f'A soma dos valores é {value1 + value2}')
    elif option == 2:
        print(f'A multiplicação dos valores é {value1 * value2}')
    elif option == 3:
        if value1 > value2:
            print(f'O maior valor é {value1}')
        elif value2 > value1:
            print(f'O maior valor é {value2}')
        else:
            print(f'Os dois valores são iguais!')
    elif option == 4:
        continue
    elif option == 5:
        break
    
