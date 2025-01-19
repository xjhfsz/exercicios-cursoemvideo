#!/usr/bin/env python
# coding: utf-8

# In[4]:


money = float(input('Quanto dinheiro você tem na carteira? '))

dolar = 3.27  # valor do dólar

# ':.2f' para arredondar
print(f'Com R$ {money} você pode comprar US$ {money / dolar:.2f}')

# TODO: criar versão que verificar o valor atual do dólar (request)
