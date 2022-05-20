# Change the names based on your list
names = [
    "rosales",
    "sison",
    "morte",
    "mendez",
    "santos",
    "lazaga",
    "caraca",
    "jimenez",
    "maglucot",
    "carmona",
    "ras, kaylo",
    "gravador",
    "eucogco",
    "ras, karlo",
    "bistis",
    "lasin",
    "repollo",
    "guardario",
    "omatang",
    "glacita",
    "manolong",
    "general",
    "rubio",
    "villamil",
    "cenas",
    "cacayuran",
    "manayaga"
]

input_mode = input('Press [E] to fill a list to be searched, press any other key to use default.\nEnter choice: ')

if input_mode.lower() == 'e':
    names.clear()

    while (True):
        name = input('Enter a name: ')

        if name.lower() != 'exit':
            names.append(name.lower())
        else:
            break

# List that will hold the names of the names that were not found
not_found = []
print('\nEnter names to find in list')

while (True):
    target = input('Enter name here: ')

    if target.lower() == 'exit':
        break

    if target.lower() in names:
        print('Found: Yes')
    else:
        not_found.append(target)

        print('Found: No')

print(f'\nNames that were not found:')
for name in not_found:
    print(f'@{name}')
