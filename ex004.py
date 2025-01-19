#!/usr/bin/env python
# coding: utf-8

# In[8]:


something = input('Digite alguma coisa: ')
print(f'O tipo primitivo dessa coisa é: {type(something)}')
print(f'Essa coisa só tem espaço? {something.isspace()}')
print(f'Essa coisa é um número? {something.isnumeric()}')
print(f'Essa coisa é alfabética? {something.isalpha()}')
print(f'Essa coisa é alfanumérica? {something.isalnum()}')
print(f'Essa coisa está em maiúsculas? {something.isupper()}')
print(f'Essa coisa está em minúsculas? {something.islower()}')
print(f'Essa coisa está capitalizada? {something.istitle()}')
