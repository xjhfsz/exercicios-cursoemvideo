from time import sleep
from random import randint

print('-' * 20 + 'JO KEN PO' + '-' * 20)
print(
    '''
    Escolhar uma opção para jogar:
    [ 1 ] PEDRA
    [ 2 ] PAPEL
    [ 3 ] TESOURA
    '''
)

options = ['PEDRA', 'PAPEL', 'TESOURA']

computer = randint(1, 3)  # computador joga de 1 até 3

player = int(input('Escolha uma opção: '))

print('-' * 20)
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
print('-' * 20)

if not player in [1, 2, 3]:
    # se o jogar não escolher uma opção válida
    print('Opção inválida! Tente novamente.')
    exit()  # encerra o programa

if computer == 1:
    if player == 1:
        result = 'EMPATE'
    elif player == 2:
        result = 'JOGADOR'
    elif player == 3:
        result = 'COMPUTADOR'
        
if computer == 2:
    if player == 1:
        result = 'COMPUTADOR'
    elif player == 2:
        result = 'EMPATE'
    elif player == 3:
        result = 'JOGADOR'
        
if computer == 3:
    if player == 1:
        result = 'JOGADOR'
    elif player == 2:
        result = 'COMPUTADOR'
    elif player == 3:
        result = 'EMPATE'

print(f'O computador escolheu: {options[computer -1]}')
print(f'Jogador escolheu: {options[player -1]}')
print('-' * 20)
print(f'VENCEDOR: {result}')
print('-' * 20)