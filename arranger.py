def arithmetic_arranger(problems, show_answers=False):
    total_problems = 0

    for problem in problems:
        parts = problem.split()
        first_number, operator, second_number = parts #int(parts[0]), parts[1], int(parts[2])
        total_problems += 1

        #print(parts, total_problems)

        if total_problems > 5:
            raise ValueError('Error: Too many problems.')
        elif operator not in ('+', '-'):
            raise ValueError("Error: Operator must be '+' or '-'.")
        elif len(first_number) > 4 or len(second_number) > 4:
            raise ValueError('Error: Numbers cannot be more than four digits.')
        else:
            print_list = []
            first_pad = 4 - len(first_number)
            second_pad = 4 - len(second_number)
            print_list = ([' '] * first_pad) + list(first_number) + list('\n') + ([' '] * second_pad) + list(second_number) + list('\n') + list('----')

            print(''.join(print_list))
        

    return problems

def main ():
    print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')

if __name__ == '__main__':
    main()