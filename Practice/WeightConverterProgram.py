weight = float(input('Weight: '))
unit = input('(L)bs or (K)g: ')

if unit.upper() == 'L':
    converted = weight * 0.4535
    print(f'You are {converted} kgs')
elif unit.upper() == 'K':
    converted = weight / 0.4535
    print(f'You are {converted} pounds')
else:
    print("Please enter valid unit")
    