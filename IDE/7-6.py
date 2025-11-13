predkosc_min = 40.0
predkosc_max = 140.0

predkosc = input('Podaj predkosc pojazdu: ')
predkosc_kmh = float(predkosc)

predkosc_dopuszczalna = (predkosc_min <= predkosc_kmh <= predkosc_max)
if predkosc_dopuszczalna:
    print(f'Speed is valid: {predkosc_dopuszczalna}')
else:
    print(f'Speed is valid: {predkosc_dopuszczalna}')