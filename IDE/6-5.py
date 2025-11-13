###
# a program that prints a 9-digit telephone number
# entered from the keyboard as three groups of 3 digits each,
# separated by a dash character.
#
phone = input('Enter phone number: ')
part1 = phone[0:3]
part2 = phone[3:6]
part3 = phone[6:9]

newphone = f'{part1}-{part2}-{part3}'

print(f'Phone number: {newphone}')