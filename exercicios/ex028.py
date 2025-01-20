from random import randint
from time import sleep

computer = randint(1, 6)  # computador joga de 1 até 5

print('-' * 20)
print('Vou pensar em um número de 1 a 5. Tente adivinhar...')
print('-' * 20)

player = int(input('Adivinha o número que pensei de 1 a 5: '))  # jogador joga

print('-' * 20)
print('Processando...')
sleep(2)

if player == computer:
    print(f'Parabéns! Você acertou o número que eu pensei! Número: {computer}')
else:
    print(f'Ganhei! Eu pensei no número {computer} e você escolheu {player}!')

