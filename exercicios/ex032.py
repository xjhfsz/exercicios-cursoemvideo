from datetime import date

year = int(input('Qual ano você quer analisar? Digite 0 para o ano atual: '))

if year == 0:  # ano atual
    year = date.today().year

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f'O ano {year} é bissexto!')
else:
    print(f'O ano {year} NÃO é bissexto!')