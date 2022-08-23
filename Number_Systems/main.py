from secrets import choice
from from_decimal import decimal_to_binary, decimal_to_octal, decimal_to_hexadecimal
from to_decimal import binary_to_decimal, octal_to_decimal, hexadecimal_to_decimal


def main():
    result = None
    start_from_top = True
    from_input = None
    input_value = None

    while(True):
        choices()

        if start_from_top:
            input_value = input('Enter value: ')
            from_input = input('Convert from: ')

        to_input = input('Convert into: ')

        if from_input == '1':
            input_value = int(input_value)

            if to_input == '1':
                result = input_value
            elif to_input == '2':
                result = decimal_to_binary(input_value)
            elif to_input == '3':
                result = decimal_to_octal(input_value)
            elif to_input == '4':
                result = decimal_to_hexadecimal(input_value)

        elif from_input == '2':
            input_value = int(input_value)
            temp_value = binary_to_decimal(input_value)

            if to_input == '1':
                result = temp_value
            elif to_input == '2':
                result = input_value
            elif to_input == '3':
                result = decimal_to_octal(temp_value)
            elif to_input == '4':
                result = decimal_to_hexadecimal(temp_value)

        elif from_input == '3':
            input_value = int(input_value)
            temp_value = octal_to_decimal(input_value)

            if to_input == '1':
                result = temp_value
            elif to_input == '2':
                result = decimal_to_binary(temp_value)
            elif to_input == '3':
                result = input_value
            elif to_input == '4':
                result = decimal_to_hexadecimal(input_value)

        elif from_input == '4':
            temp_value = hexadecimal_to_decimal(input_value)

            if to_input == '1':
                result = temp_value
            elif to_input == '2':
                result = decimal_to_binary(temp_value)
            elif to_input == '3':
                result = decimal_to_octal(temp_value)
            elif to_input == '4':
                result = input_value

        print(f'The result is {result}')
        repeat = input("Press [C] to convert into another system, press [R] to restart: ")

        if repeat.lower() == 'c':
            input_value = result
            from_input = to_input
            start_from_top = False
        elif repeat.lower() == 'r':
            start_from_top = True
        else:
            print('Thanks for using')
            break
    

def choices():
    print(
        '''
        Select the number of choice

        [1] Decimal
        [2] Binary
        [3] Octal
        [4] Hexadecimal
        '''
    )


if __name__ == '__main__':
    main()