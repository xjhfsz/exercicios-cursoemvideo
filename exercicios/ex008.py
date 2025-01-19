#!/usr/bin/env python
# coding: utf-8

# In[6]:


metros = int(input('Digite uma distância em metros: '))
print(f'A medida de {metros} metros corresponde a:')

print(f'{metros * 1000} milímetros (mm)')
print(f'{metros * 100} centímetros (cm)')
print(f'{metros * 10} decímetros (dm)')
print(f'{metros / 10} decâmetros (dam)')
print(f'{metros / 100} hectômetros (hm)')
print(f'{metros / 1000} quilômetros (km)')
