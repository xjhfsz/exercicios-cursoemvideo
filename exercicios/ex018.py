import math

angle = float(input('Digite um ângulo em graus: '))

sen = math.sin(math.radians(angle))
cos = math.cos(math.radians(angle))
tan = math.tan(math.radians(angle))

print('-' * 15)
print(f'O ângulo de {angle}° tem Seno de: {sen:.2f}')
print(f'O ângulo de {angle}° tem Cosseno de: {cos:.2f}')
print(f'O ângulo de {angle}° tem Tangente de: {tan:.2f}')