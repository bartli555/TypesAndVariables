###
# The program calculates the cost of transporting goods
# based on the given distance in km, fuel price per 1 liter,
# and fuel consumption in liters per 100 km.
#
distance = int(input('Enter distance in km: '))
fuel_price = float(input('Enter fuel price per liter: '))
fuel_consumption = float(input('Enter fuel consumption in liters per 100 km: '))
total_fuel_consumption = (fuel_consumption / 100) * distance #przeliczenie konsumpcji paliwa na 1km
total_cost = total_fuel_consumption * fuel_price #to całkowity koszt transportu (cena paliwa za 1km razy liczba kilometrów)
print(f'Distance: {distance} km')
print(f'Fuel Price: {fuel_price}')
print(f'Fuel Consumption: {fuel_consumption} L/100km')
print(f'Total cost of transport: {total_cost:.2f}')
