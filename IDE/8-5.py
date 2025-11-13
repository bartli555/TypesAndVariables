swift = input('Podaj kod Swift: ')

swift = swift.upper()

kod_banku = swift[0:4]

kod_kraju = swift[4:6]

print(f'Bank Code: {kod_banku}')
print(f'Country Code:{kod_kraju}')