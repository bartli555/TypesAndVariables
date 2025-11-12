cena_str = input('Wprowadz cene produktu:')
cena = float(cena_str)
rabat_str = input('Wprowadz ile rabatu w %:')
rabat = float(rabat_str)

rabat_kwota = cena * (rabat / 100)
cena_po_rabacie = cena - rabat_kwota

print(f'Cena początkowa wynosi: {cena}')
print(f'Rabat wynosi: {rabat}%')
print(f'Cena po rabacie wynosi: {cena_po_rabacie:.2f}')
print(f'Róznica w cenie wynosi: {rabat_kwota:.2f}')