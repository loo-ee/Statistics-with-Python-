# Mean Median Mode Implementation

def input_values(x: list, r: list):
    loop = True
    weighted_status = False

    x.clear()
    is_weighted = input("Press [W] if you want to input reference set: ")
    print('\nInput "STOP" to stop appending elements')

    if is_weighted.lower() == 'w':
        weighted_status = True
    
    while loop:
        try:
            element_input = input("Enter values for set: ")

            if element_input.lower() == "stop":
                loop = False
            else:
                x.append(int(element_input))

                if is_weighted.lower() == 'w':
                    r.append(int(input("Enter reference value: ")))
                    print()
        except Exception:
            print("[INFO] You have an invalid input of string, please try again.")

    print()
    return weighted_status


def mean(x: list):
    list_sum = 0
    mean = 0

    for i in range (0, len(x)):
        list_sum += x[i]
    
    mean = float(list_sum / len(x))

    print(f'''
    Solution:
    Mean = ∑X/N
    = (''', end='')

    for i in range (0, len(x)):
        print(f'{x[i]}', end='')

        if i != len(x) - 1:
            print(' + ', end='')

    print(f''') / {len(x)}
    = {list_sum}/{len(x)}
    = {mean}''')

    print(f"\nThe mean is {mean}.")


def median(x: list):
    temp_x_list = []
    temp = 0
    median = 0
    set_len = len(x)
    indice = int(set_len/2)

    for i in range (0, set_len):
        temp_x_list.append(x[i])

    print(f'\nSolution:\nThe list (', end='')

    for i in range(0, set_len):
        print(f'{x[i]}', end='')

        if i != set_len -1:
            print(', ', end='')

    print(f') contains {set_len} numbers.\nRanking the numbers from smallest to largest gives (', end='')

    for i in range (0, set_len):
        for j in range (0, set_len-1):
            if (temp_x_list[j] > temp_x_list[j+1]):
                temp = temp_x_list[j]
                temp_x_list[j] = temp_x_list[j+1]
                temp_x_list[j+1] = temp

    for i in range (0, set_len):
        print(f'{temp_x_list[i]}', end='')

        if i != set_len - 1:
            print(', ', end='')

    print(f'''). The middle ''', end='')

    if (len(x) % 2) == 0:
        median = float((temp_x_list[indice-1] + temp_x_list[indice]) /2)
        print(f'numbers are {temp_x_list[indice-1]} and {temp_x_list[indice]}.\nThus {median} is the median, which is the mean of the two middle numbers.')

    else:
        median = temp_x_list[indice]
        print(f'number is {temp_x_list[indice]}.\nThus {median} is the median.')


def mode(x: list):
    mode = []
    x_list = []
    highest_value = 0
    mode_type = ""

    for i in range(0, len(x)):
        count = 0

        for j in range(0, len(x)):
            if x[i] == x[j]:
                count += 1
        
        x_list.append(count)

    
    for i in range (0, len(x_list)):
        if x_list[i] > highest_value and x_list[i] > 1:
            highest_value = x_list[i]

    for i in range (0, len(x_list)):
        if highest_value == x_list[i] and x[i] != 0:
            if x[i] not in mode:
                mode.append(x[i])

    print(f'Solution:\nIn the list (', end='')

    for i in range (0, len(x_list)):
        print(f'{x[i]}', end='')

        if i != len(x_list) - 1:
            print(', ', end='')

    if (len(mode)) == 1:
        mode_type = "Unimodal"
        print(f") the element {mode} occurs more often than the other numbers.\nThus {mode} is the mode.")

    elif (len(mode)) == 2:
        mode_type = "Bimodal"
        print(f") the elements {mode} occurs more often than the other numbers.\nThus {mode} are the modes.")


    elif (len(mode)) > 2:
        mode_type = "Multimodal"
        print(f") the elements {mode} occurs more often than the other numbers.\nThus {mode} are the modes.")

    else:
        mode_type = "Non-modal"
        print(f") all elements occur only once.\nThus there is no mode.")

    print(f"Mode type is {mode_type}.")


def weighted_mean(x: list, r: list, is_weighted: bool):
    list_sum = 0
    reference_sum = 0
    mean = 0

    if (not is_weighted):
        print("Reload entire program first and input reference list!")
        return

    for i in range (0, len(x)):
        list_sum += x[i] * r[i]
        reference_sum += r[i]

    mean = float(list_sum / reference_sum)

    print(f'''Solution:
    Weighted Mean = ∑ ( X * W) / ∑W
    = [''', end='')

    for i in range (0, len(x)):
        print(f'({x[i]}x{r[i]}) + ', end='')

    print(f'''] / {reference_sum}
    = {list_sum} / {reference_sum}
    Weighted mean: {mean}''')


data_set = []
reference_set = []
onLoop = True
firstRun = True

while onLoop:

    if firstRun:
        is_weighted = input_values(data_set, reference_set)
        firstRun = False

    print('''[OPERATIONS]
        [1] Mean
        [2] Median
        [3] Mode
        [4] Weighted Mean
        ''')
    choice = input("Select operation: ")

    if choice.lower() == '1':
        mean(data_set)

    elif choice.lower() == '2':
        median(data_set)

    elif choice.lower() == '3':
        mode(data_set)

    elif choice.lower() == '4':
        weighted_mean(data_set, reference_set, is_weighted)

    else:
        print("You have entered an invalid choice, please try again.")

    reloadProgram = input("\nPress [R] to reload entire program\nPress [C] to select another operation\nPress [E] to exit program\nChoice: ")

    if reloadProgram.lower() == 'r':
        firstRun = True

    elif reloadProgram.lower() == 'e':
        onLoop = False

    else:
        print("You have entered an invalid input, please try again.")

    print()

print("Thank you for using the program!")
