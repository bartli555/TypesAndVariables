vat_percent = 23
vat = vat_percent / 100

print(f'Procent Vat wynosi: {vat_percent}%')

brutto_str = input('Wprowadź kwotę brutto: ')
brutto = float(brutto_str)

netto = brutto / (1 + vat)
kwota_vat = brutto - netto

print(f'Kwota brutto wynosi: {brutto:.2f}')
print(f'Kwota netto wynosi: {netto:.2f}')
print(f'Wartośc Vat wynosi: {kwota_vat:.2f}')