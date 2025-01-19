#!/usr/bin/env python
# coding: utf-8

# In[ ]:


price = float(input('Qual o preço do produto? R$ '))

discount = 5  # desconto de 5%

new_price = price - (price * (discount / 100))

print(f'O produto que custava R$ {price:.2f}, na promoção com desconto de {discount}% vai custar R$ {new_price:.2f}')
