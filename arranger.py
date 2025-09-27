def arithmetic_arranger(problems: list[str], show_answers: bool = False) -> str:
    """Arranges a list of arithmetic problems vertically and side-by-side.

    This function takes a list of arithmetic problems (as strings) and
    formats them into a multi-line string, similar to how a person 
    would solve them on paper.

    Args:
        problems (list[str]): A list of strings, each representing an
            addition or subtraction problem. Limited to 5 problems.
        show_answers (bool): If set to True, the answers to the problems
            will be displayed on a fourth line. Defaults to False.

    Returns:
        str: A single, multi-line string containing the formatted
             problems, or an error message string if the input is invalid.
    """
    if len(problems) > 5:
        return 'Error: Too many problems.'

    first_row_parts = []
    second_row_parts = []
    third_row_parts = []
    fourth_row_parts = []

    for problem in problems:
        parts = problem.split()
        first_number, operator, second_number = parts

        # --- Guard Clauses ---
        if operator not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."
        if not first_number.isdigit() or not second_number.isdigit():
            return 'Error: Numbers must only contain digits.'
        if len(first_number) > 4 or len(second_number) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        # --- Formatting the current problem ---
        pad = max(len(first_number), len(second_number)) + 2
        first_row_parts.append(f'{first_number:>{pad}}')
        second_row_parts.append(f'{operator}{second_number:>{pad - 1}}')
        third_row_parts.append('-' * pad)

        # --- Perform calculation only if answer required ---
        if show_answers:
            if operator == '+':
                answer = int(first_number) + int(second_number)
            else:
                answer = int(first_number) - int(second_number)
        
            fourth_row_parts.append(f'{str(answer):>{pad}}')

    # --- Assemble the final output strings ---
    separator = '    '
    first_line = separator.join(first_row_parts)
    second_line = separator.join(second_row_parts)
    third_line = separator.join(third_row_parts)

    arranged_problems = f'{first_line}\n{second_line}\n{third_line}'

    if show_answers:
        fourth_line = separator.join(fourth_row_parts)
        arranged_problems += f'\n{fourth_line}'

    return arranged_problems

def main ():
    """Defines and runs a series of test cases for the arithmetic_arranger function."""

    # --- Standard Test Cases (Without Answers) ---

    # Test case 1: Standard two problems
    print(f'\n{arithmetic_arranger(["3801 - 2", "123 + 49"])}')

    # Test case 2: Standard two problems with different lengths
    print(f'\n{arithmetic_arranger(["1 + 2", "1 - 9380"])}')

    # Test case 3: Standard four problems
    print(f'\n{arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"])}')

    # Test case 4: Standard five problems (the maximum allowed)
    print(f'\n{arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"])}')

    # --- Error Handling Test Cases ---

    # Test case 5: Should return "Error: Too many problems."
    print(f'\n{arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"])}')

    # Test case 6: Should return "Error: Operator must be '+' or '-'."
    print(f'\n{arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"])}')

    # Test case 7: Should return "Error: Numbers cannot be more than four digits."
    print(f'\n{arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"])}')

    # Test case 8: Should return "Error: Numbers must only contain digits."
    print(f'\n{arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"])}')

    # --- Test Cases With Answers ---

    # Test case 9: Standard call with answers requested
    print(f'\n{arithmetic_arranger(["3 + 855", "988 + 40"], True)}')

    # Test case 10: Five problems with answers requested
    print(f'\n{arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)}')

if __name__ == '__main__':
    main()