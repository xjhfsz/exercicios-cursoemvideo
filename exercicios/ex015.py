#!/usr/bin/env python
# coding: utf-8

# In[6]:


print('-' * 7 + ' ALUGUEL DE CARROS ' + '-' * 7)

days = int(input('Quantos dias alugado? '))
km = float(input('Quantos km rodados? '))

# 60 reais por dia
# 0,15 reais por km
price = (60 * days) + (0.15 * km)

print('-' * 20)
print(f'O veículo foi alugado por {days} dias e rodou {km} km')
print(f'O preço a pagar é de R${price:.2f}')
