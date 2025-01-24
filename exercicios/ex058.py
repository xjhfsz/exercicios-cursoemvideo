from random import randint
from time import sleep

print('-' * 10 + ' JOGO DA ADIVINHAÇÃO v2.0 ' + '-' * 10)

computer = randint(0, 10)  # computador joga de 1 até 10

guess_count = 0  # contador de tentativas

success = False  # variável de sucesso/acerto

print('Tente adivinhar o número que eu pensei de 0 a 10!')
print('-' * 20)

while not success:
    player = int(input('Qual seu palpite de 0 a 10? '))
    guess_count += 1  # contagem + (contagem + 1)
    
    if player == computer:
        print(f'Parabéns! Você acertou o número que eu pensei! Número: {computer}')
        print(f'Você precisou de {guess_count} tentativas para acertar o número!')
        success = True  # acertou!
        
    else:
        if player < computer:
            print('Errou! Escolha um número MAIOR... ')
        elif player > computer:
            print('Errou! Escolha um número MENOR...')