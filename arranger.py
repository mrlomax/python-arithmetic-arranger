def arithmetic_arranger(problems, show_answers=False):
    first_row_list = []
    second_row_list = []
    third_row_list = []
    fourth_row_list = []
    output = []

    if len(problems) > 5:
        return('Error: Too many problems.')

    for i, problem in enumerate(problems):
        parts = problem.split()
        first_number, operator, second_number = parts

        if operator not in ('+', '-'):
            return("Error: Operator must be '+' or '-'.")
        elif not first_number.isdigit() or not second_number.isdigit():
            return('Error: Numbers must only contain digits.')
        elif len(first_number) > 4 or len(second_number) > 4:
            return('Error: Numbers cannot be more than four digits.')
        else:
            pad = max(len(first_number), len(second_number)) + 2
            first_row_list.extend(([' '] * (pad - len(first_number))) + list(first_number))
            second_row_list.extend(list(operator) + ([' '] * (pad - len(second_number) - 1)) + list(second_number))
            third_row_list.extend((['-'] * pad))

            if operator == '+':
                answer = int(first_number) + int(second_number)
            elif operator == '-':
                answer = int(first_number) - int(second_number)
            
            fourth_row_list.extend(([' '] * (pad - len(str(answer))) + list(str(answer))))

            if i < len(problems):
                first_row_list.extend('    ')
                second_row_list.extend('    ')
                third_row_list.extend('    ')
                fourth_row_list.extend('    ')

    output.extend(first_row_list + list('\n') + second_row_list + list('\n') + third_row_list)
    if show_answers == True:
        output.extend(list('\n') + fourth_row_list)

    return ''.join(output)

def main ():
    print(f'\n{arithmetic_arranger(["3801 - 2", "123 + 49"])}')

if __name__ == '__main__':
    main()