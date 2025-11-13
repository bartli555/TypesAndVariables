import random

dice_roll = random.randint(1,6)
print(f'Dice rolled: {dice_roll}')

if dice_roll == 1 or dice_roll == 6:
    print(f'Special number (1 to 6): {True}')
else:
    print(f'Special number (1 to 6): {False}')