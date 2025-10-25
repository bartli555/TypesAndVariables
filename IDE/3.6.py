import math

def oblicz(h_metry):
    stala = 3.57
    odleglosc = stala * math.sqrt(h_metry)
    return odleglosc

try:

    wysokosc = float(input("Podaj wysokosc obserwatora: "))
    odleglosc_do_horyzontu = oblicz(wysokosc)

    print("Na wysokkoci {wysokosc} m,")
    print("Horyzont znajduje sie na wysokosci {odleglosc_do_horyzontu:.2f} km")