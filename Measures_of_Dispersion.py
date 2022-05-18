# Finding the Range, Standard Deviation, and Variance
from cmath import sqrt


def main():
    data_list = []

    choice = input("Press [1] to solve for SD for Population\nPress [2] to solve for SD for Sample\nInput: ")
    input_values(data_list)

    data_list_range = solve_for_range(data_list)

    if choice == '1':
        without_sqrt = solve_for_population_or_sample(data_list, True)
        square_root = sqrt(without_sqrt)
        
        print(f'The range for the population is {data_list_range}.')
        print(f'The standard deviation for the population of (', end='')

        for i in range (0, len(data_list)):
            print(data_list[i], end='')

            if i != len(data_list) - 1:
                print(' , ', end='')

        print(f') is {square_root}.')
        print(f'The deviance is {without_sqrt}.')

    elif choice == '2':
        without_sqrt = solve_for_population_or_sample(data_list, False)
        square_root = sqrt(without_sqrt)
        
        print(f'The range for the sample is {data_list_range}.')
        print(f'The standard deviation for the sample of (', end='')

        for i in range (0, len(data_list)):
            print(data_list[i], end='')

            if i != len(data_list) - 1:
                print(' , ', end='')

        print(f") is {square_root}")
        print(f"The variance is {without_sqrt}")

    print()


def solve_for_range(data: list):
    least_val = data[0]
    max_val = data[0]

    for i in range(0, len(data)):
        if data[i] < least_val:
            least_val = data[i]
        if data[i] > max_val:
            max_val = data[i]

    return max_val - least_val


def solve_for_population_or_sample(data: list, is_population: bool):
    temp_list = []
    list_mean = mean(data)
    list_sum = 0

    print()

    for i in range(0, len(data)):
        difference = data[i] - list_mean
        print(f'{data[i]} - ' + '{:.3f}'.format(round(list_mean, 3)) + ' = {:.3f}'.format(round(difference, 3)) + '\t', end='')
        # print(f'{data[i]} - {list_mean} = {difference}\t', end='')
        square = pow(difference, 2)
        print('{:.3f}'.format(round(square, 3)))
        temp_list.append(square)
        list_sum += square

    print('\nSum = ' + '{:.3f}'.format(round(list_sum, 3)))

    if is_population:
        return list_sum / len(data)
    
    return list_sum / (len(data) - 1)


def input_values(data: list):
    loop = True

    data.clear()
    print('\nInput "STOP" to stop appending elements')
    
    while loop:
        try:
            element_input = input("Enter values for set: ")

            if element_input.lower() == "stop":
                loop = False
            else:
                data.append(int(element_input))

        except Exception:
            print("[INFO] You have an invalid input of string, please try again.")

    print()


def mean(data: list):
    list_sum = 0
    mean = 0

    for i in range (0, len(data)):
        list_sum += data[i]
    
    mean = float(list_sum / len(data))

    print(f'''
    Solution:
    Mean = ∑X/N
    = (''', end='')

    for i in range (0, len(data)):
        print(f'{data[i]}', end='')

        if i != len(data) - 1:
            print(' + ', end='')

    print(f''') / {len(data)}
    = {list_sum}/{len(data)}
    = {mean}''')

    print("\nThe mean is " + "{:.3f}".format(round(mean, 3)))

    return mean


if __name__ == "__main__":
    main()
    