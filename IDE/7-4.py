import math

wymagana_srednica = 50.0

obwod = input('Podaj obwód drzewa w cm: ')
obwod_cm = float(obwod)

srednica = obwod_cm / math.pi

mozna_sciac = (srednica >= wymagana_srednica)

print(f' Tree circumference: {obwod}')
print(f'Drzewo można sciąć: {mozna_sciac}')