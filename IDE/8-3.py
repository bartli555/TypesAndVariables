###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#

celcius_str = input('Podaj temperaturę w celsjuszach: ')  # definiujemy celsjusza
celcius = float(celcius_str)

kelvin = float()  # definiujemy kelviny i fahrenheity
kelvin = celcius + 273.15

fahrenheit = float()
fahrenheit = (celcius * 1.8) + 32

print(f'Temperatura w Celsjuszach to: {celcius:.2f}') # drukujemy wyniki
print(f'Temepratura w Kelvinach to: {kelvin:.2f}')
print(f'Temperatura w fahrenheitach to: {fahrenheit:.2f}')