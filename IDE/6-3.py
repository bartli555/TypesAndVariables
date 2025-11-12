###
# A program that prints a university abbreviation
#   
university = "Krakow University of Economics"
slowa = university.split()
skrot =''

for slowo in slowa:
    if slowo and slowo[0].isupper():
        skrot = skrot + slowo[0]

print(f'{skrot}')        