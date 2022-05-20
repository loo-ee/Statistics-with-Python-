# The Language of Sets Python Implementation


def choices():
    print("""   Check if:
        [1] Empty set
        [2] Subset
        
    Operations on sets:
        [3] Union
        [4] Intersection
        [5] Set Difference
        [6] Complement
        [7] Cartesian Product
        [8] Set Builder
    """)


def set_sets(u: list, x: list, y: list, z: list):
    print("Set Values for Universal set")
    input_values(u)
    print("Set Values for set A")
    input_values(x)
    print("Set Values for set B")
    input_values(y)
    print("Set values for set C")
    input_values(z)


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


def check_if_null(x: list):
    if not x:
        return False

    return True


def check_subset(x: list, y: list):
    is_a_subset = True

    if not x:
        return False

    for element in range(0, len(x)):
        if x[element] not in y:
            is_a_subset = False

    return is_a_subset


def union(x: list, y: list, z: list):
    unified_set = x

    for element in range(0, len(y)):
        if y[element] not in unified_set:
            unified_set.append(y[element])

    choice = input("Press [A] to add third set: ")

    if choice.lower() == 'a':
        for element in range(0, len(z)):
            if z[element] not in unified_set:
                unified_set.append(z[element])

    else:
        print("Third set skipped...")

    print("Operation done successfully!")
    choice = input("Press [S] to display unified list: ")

    if choice.lower() == 's':
        print("{", end='')

        for element in range(0, len(unified_set)):
            print(unified_set[element], end=',')

        print('}')


def intersection(x: list, y: list):
    intersected_list = []

    for element in range(0, len(x)):
        if x[element] in y:
            if x[element] not in intersected_list:
                intersected_list.append(x[element])

    print("Operation done successfully!")
    choice = input("Press [S] to display intersected list: ")

    if choice.lower() == 's':
        print("{", end='')

        for element in range(0, len(intersected_list)):
            print(intersected_list[element], end=',')

        print('}')


def set_difference(x: list, y: list):
    difference_list = []

    for element in range(0, len(x)):
        if x[element] not in y:
            difference_list.append(x[element])

    print("Operation done successfully!")
    choice = input("Press [S] to display differentiated list: ")

    if choice.lower() == 's':
        print("{", end='')

        for element in range(0, len(difference_list)):
            print(difference_list[element], end=',')

        print('}')


def complement(universal: list, x: list):
    complement_set = []

    for element in range(0, len(universal)):
        if universal[element] not in x:
            complement_set.append(universal[element])

    print("Operation done successfully!")
    choice = input("Press [S] to display complement list: ")

    if choice.lower() == 's':
        print("{", end='')

        for element in range(0, len(complement_set)):
            print(complement_set[element], end=',')

        print('}')


def cartesian_product(x: list, y: list):
    print('{', end='')

    for element in range(0, len(x)):
        for index in range(0, len(y)):
            # cartesian_list.append([x[element], y[index]])
            print(f'({x[element]}, {y[index]})', end=',')

    print('}')


def set_builder(u: list):
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    u.clear()

    print("Press [A] for alphabet\nPress [N] for numbers")
    choice = input("Choice : ")

    if choice.lower() == 'a':
        for element in range(0, len(alphabet)):
            u.append(alphabet[element])
    elif choice.lower() == 'n':
        limit = int(input("Enter limit: "))

        for element in range(1, limit+1):
            u.append(str(element))

    print("Operation done successfully")
    print(u)


def main():
    universal_set = []
    set_a = []
    set_b = []
    set_c = []
    main_loop = True
    first_run = True

    while main_loop:

        if first_run:
            set_sets(universal_set, set_a, set_b, set_c)
            first_run = False

        choices()
        user_input = input("Enter choice: ")

        if user_input == '1':
            if (check_if_null(universal_set)) and (check_if_null(set_a)) and \
                    (check_if_null(set_b)) and (check_if_null(set_c)):
                print("Sets are empty")
            else:
                print("All sets are not empty")

        elif user_input == '2':
            if check_subset(set_a, set_b):
                print("Set Y is a subset of set A")
            else:
                print("Set B is not a a subset of set A")

        elif user_input == '3':
            union(set_a, set_b, set_c)

        elif user_input == '4':
            intersection(set_a, set_b)

        elif user_input == '5':
            set_difference(set_a, set_b)

        elif user_input == '6':
            complement(universal_set, set_a)

        elif user_input == '7':
            cartesian_product(set_a, set_b)

        elif user_input == '8':
            set_builder(universal_set)

        else:
            print("You have entered an invalid input. Please try again")

        input_error = True

        while input_error:
            print("\nPress [R] to reload program\nPress [C] to select another choice"
                  "\nPress [E] to exit")
            reload_program = input("Input: ")

            if reload_program.lower() == 'r':
                first_run = True
                input_error = False
                print()
            elif reload_program.lower() == 'c':
                input_error = False
                print()
            elif reload_program.lower() == 'e':
                main_loop = False
                input_error = False
                print("Thank you for using the program")
            else:
                print("You have entered a wrong input, please try again")


if __name__ == '__main__':
    main()
