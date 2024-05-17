import random

names = ['Leonard', 'Penny', 'Sheldon', 'Howard', 'Amy', 'Bernadatte', 'Raj']

print(f'Bill will be paid by {names[random.randint(0, len(names)-1)]}')
print(f'Bill will be paid by {random.choice(names)}')

print(f'Names before shhuffling: {names}')
random.shuffle(names)
print(f'Names after shhuffling: {names}')
