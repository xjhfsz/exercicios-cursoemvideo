sentence = str(input('Digite uma frase: ')).strip().upper()

print('-' * 20)
print(f'A letra "A" aparece {sentence.count("A")} vezes na frase.')
print(f'A primeira letra "A" apareceu na posição {sentence.find("A") + 1}.')
print(f'A ultima letra "A" apareceu na posição {sentence.rfind("A") + 1}.')