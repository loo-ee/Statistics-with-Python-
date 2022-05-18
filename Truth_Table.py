# Truth Table Python Implementation

def conjunction(p, q):
    if p and q == 'True':
        return 'True'
    else:
        return 'False'


def disjunction(p, q):
    if p or q == 'True':
        return 'True'
    elif p and q == 'False':
        return 'False'


def exclusive_or(p, q):
    if (p == 'True' and q == 'False') or (p == 'False' and q == 'True'):
        return 'True'
    else:
        return 'False'


def implication(p, q):
    if p == 'True' and q == 'False':
        return 'False'
    else:
        return 'True'


def biconditional(p, q):
    if p == q:
        return 'True'
    else:
        return 'False'


def table_of_choices():
    print("""
    Select from List:
    [1] Conjunction     (p^q)
    [2] Disjunction     (opposite of p^q)
    [3] Exclusive 'or'  ( (+) )
    [4] Implication     (p->q)
    [5] Biconditional   (p<->q)
    """)


def main():
    conversion_mode = input("Press [T] for table format, or press [I] for individual: ")

    if conversion_mode == 't' or 'T':
        number_of_values = int(input("Enter how many rows: "))
        p_array = []
        q_array = []

        print("\nPress [1] for true, [2] for false")
        print("Enter values for p: ")

        for index in range(number_of_values):
            p_array.append(input(f"P #{index + 1}: "))

        print("\nEnter values for q: ")

        for index in range(number_of_values):
            q_array.append(input(f"Q #{index + 1}: "))

        table_of_choices()
        choice = input("Enter choice: ")

        print("\n[Showing Results]")

        for index in range(number_of_values):
            if p_array[index] == '1':
                p_array[index] = 'True'
            elif p_array[index] == '2':
                p_array[index] = 'False'

            if q_array[index] == '1':
                q_array[index] = 'True'
            elif q_array[index] == '2':
                q_array[index] = 'False'

            if choice == '1':
                print(
                    f"Row #{index + 1}: {conjunction(p_array[index], q_array[index])}\t| where p = {p_array[index]} and\tq = {q_array[index]}")
            elif choice == '2':
                print(
                    f"Row #{index + 1}: {disjunction(p_array[index], q_array[index])}\t| where p = {p_array[index]} and\tq = {q_array[index]}")
            elif choice == '3':
                print(
                    f"Row #{index + 1}: {exclusive_or(p_array[index], q_array[index])}\t| where p = {p_array[index]} and\tq = {q_array[index]}")
            elif choice == '4':
                print(
                    f"Row #{index + 1}: {implication(p_array[index], q_array[index])}\t| where p = {p_array[index]} and \tq = {q_array[index]}")
            elif choice == '5':
                print(
                    f"Row #{index + 1}: {biconditional(p_array[index], q_array[index])}\t| where p = {p_array[index]} and \tq = {q_array[index]}")

    elif conversion_mode == 'i' or 'I':
        print("Press [1] for true, [2] for false")
        p = input("Value for p: ")
        q = input("Value for q: ")

        if p == '1':
            p = 'True'
        elif p == '2':
            p = 'False'

        if q == '1':
            q = 'True'
        elif q == '2':
            q = 'False'

        table_of_choices()
        choice = input("Enter choice: ")

        if choice == '1':
            print("Result of Conjunction: " + conjunction(p, q))
        elif choice == '2':
            print("Result of Disjunction: " + disjunction(p, q))
        elif choice == '3':
            print("Result of Eclusive 'or': " + exclusive_or(p, q))
        elif choice == '4':
            print("Result of Implication: " + implication(p, q))
        elif choice == '5':
            print("Result of Biconditional: " + biconditional(p, q))

    repeat_program = input("\nPress [R] to repeat program: ")

    if repeat_program == 'r' or 'R':
        print()
        main()


if __name__ == '__main__':
    main()
