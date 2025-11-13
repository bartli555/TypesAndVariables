###
# A program that prints your height both in cm and in feet and inches.
#
cm = 170

inch_in_cm = 2.54 #przeliczniki 
feet_in_inch = 12

total_inches = round(cm/inch_in_cm) #round zaokrągla do "najbliższego" cala

feet = total_inches // feet_in_inch #podział na "pełne stopy" czyli // oraz reszte z dzielenie czyli % "cale"
inches = total_inches % feet_in_inch
# calculate the number of feet

print(f'I am {cm}cm tall, i.e. {feet} feet and {inches} inches')