# using fundamentals in a simple quest

# weight converter program
# ask the user to add their weight
# ask if the weight is in kilos or lbs
weight = int(input('Weight: '))
unit = input('(K)g or (L)lbs: ')

if unit.upper() == 'L':
    converted = weight * 0.45
    print('Weight in kilos: ' + str(converted))
else:
    converted = weight / 0.453592
    print('Weight in lbs: ' + str(converted))