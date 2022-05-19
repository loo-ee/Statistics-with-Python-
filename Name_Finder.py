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
    "Manayaga"
]

# List that will hold the names of the names that were not found
not_found = []

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
