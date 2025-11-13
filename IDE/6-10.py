###
# String manipulation
#

movie = "The Lord of the Rings: The Return of the King"

# print number of characters
print('Number of characters: ', len(movie))

# print title in capital letters
duze = movie.upper()
print('Title in capital letters: ', (duze))

# print title in small letters
male = movie.lower()
print('Title in capital letters: ', (male))

# print how many times the vowel "e" appears in the title
letter_e = movie.count('e')
print(f'Vovel "e" appers: {letter_e} times')

# print where in the text is the word "Lord"
lord = movie.find('Lord')
print(f'Word "Lord" is on the {lord} position')

# print where in the text is the word "dragon"
dragon = movie.find('dragon')
print(f'Word "dragon" is on the {dragon} position')
if dragon == -1:
    print('The word dragon does not appear')