liczba_dziesietna_str = input('Wprowadź liczbę dziesiętną: ')
liczba_dziesietna = int(liczba_dziesietna_str)

binarna = bin(liczba_dziesietna)
szesnastkowa = hex(liczba_dziesietna)

print(f'Liczba dziesiętna to: {liczba_dziesietna}')
print(f'Liczba binarna to: {binarna}')
print(f'Liczba szesnastkowa to: {szesnastkowa}')