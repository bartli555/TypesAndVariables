###
# Calculation of circle area and circumference 
#

PI = 3.14 # determine radius and PI values
radius_input = input('Podaj promien kola: ')
radius = float(radius_input)

area = PI * (radius ** 2) # calculate area 

circumference = 2 * PI * radius # calculate circumference 

print(f'Dla promienia: {radius}') # print results
print(f'Pole powierzchni wynosi: {area}')
print(f'Obwód wynosi: {circumference}')