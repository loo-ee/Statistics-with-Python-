# Finding the set of ordered pairs given that the abscissa and ordinate are present

def input_values(x: list):
    loop = True

    x.clear()

    print('Input "STOP" to stop appending elements')

    while loop:
        element_input = input("Enter values for set: ")

        if element_input.lower() == "stop":
            loop = False
        else:
            x.append(element_input)
    print()


def cartesian_product(x: list, y: list):
    print('{', end='')

    for element in range(0, len(x)):
        for index in range(0, len(y)):
            print(f'({x[element]}, {y[index]})', end=',')
    print('}\n')


def user_defined_function_for_main(x: list, y: list):
    x_integers = []
    y_integers = []

    choice = input("Do you want to turn elements into integers? (Y/N): ")
    if choice.lower() == 'y':
        for element in range(0, len(x)):
            x_integers.append(int(x[element]))
            y_integers.append(int(y[element]))
    print('{', end='')

    for element in range(0, len(x_integers)):
        for index in range(0, len(y_integers)):
            # answer = ((x_integers[element] - y_integers[index]) / 3)
            # answer = x_integers[element] + y_integers[index]
            # answer = float(y_integers[index] / x_integers[element])
            answer = float((x_integers[element] - y_integers[index]) / 4)
            if answer % 1 == 0:
                print(f'({x_integers[element]}, {y_integers[index]}), ', end='')
    print('}')


main_set = []
abscissa = []
ordinate = []

print("Enter values for X coordinate")
input_values(abscissa)
print("Enter values for Y coordinate")
input_values(ordinate)

print("Showing the set of ordered pairs")
cartesian_product(abscissa, ordinate)

print("Showing the set or ordered pairs with rules on criteria")
user_defined_function_for_main(abscissa, ordinate)




