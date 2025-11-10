import math

def oblicz(metry):
    stala = 3.57

    if metry < 0:
        return 0

    odleglosc = stala * math.sqrt(metry)
    return odleglosc

try:
    wysokosc = float(input("Podaj wysokosc obserwatora w metrach: "))
    odleglosc_do_horyzontu = oblicz(wysokosc)

    print(f"Na wysokkoci {wysokosc} m,")
    print(f"Horyzont znajduje sie na wysokosci {odleglosc_do_horyzontu:.2f} km")

except ValueError:
    print("Błąd: Wprowadzona wartość nie jest poprawną liczbą.")
