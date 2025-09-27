# Arithmetic Formatter

This is a Python script I wrote to complete the Arithmetic Formatter certification project. The function takes a list of arithmetic problems and returns them arranged vertically and side-by-side, as if written on a worksheet. This project was a great opportunity to combine all the best practices I've learned into a single, polished program.



## Skills Demonstrated

This project served as a practical exercise in building a complete, robust function from scratch, focusing on the following key skills:

- **String Parsing and Manipulation:** Deconstructing problem strings using `.split()` and validating their contents with methods like `.isdigit()`.

- **Advanced F-String Formatting:** Leveraging f-strings not just for embedding variables, but for applying complex alignment and padding (`:>{width}`) to produce a clean, formatted, multi-line output.

- **Robust Error Handling:** Implementing a series of **guard clauses** at the beginning of the function to validate all input conditions (problem count, operator type, number length, and character type) and return clear error messages.

- **Clean Algorithmic Logic:** Iterating through the list of problems, building lists of formatted string components for each row, and then efficiently assembling the final multi-line output using the `str.join()` method.

- **Professional Documentation:** Writing a comprehensive multi-line **docstring** to explain the function's purpose, arguments, and return value, and using modern **type hints** to ensure code clarity and safety.

## Features

- Formats up to five addition or subtraction problems.
- Right-aligns numbers in a visually appealing, vertical arrangement.
- Includes robust error handling for invalid input (wrong operator, non-digit characters, incorrect length, etc.).
- Optionally calculates and displays the answer to each problem.

## Requirements

This script uses only Python's standard library, so no external packages are needed. All you need is **Python 3.x** installed.

## Usage

To run the script with the built-in examples, save the code as `arranger.py` and execute it from your terminal:

```sh
python arranger.py
```

This will run the `main()` function, which includes several test cases. The output for a set of five problems with answers displayed is:

```
   32         1      45      123      988
- 698    - 3801    + 43    +  49    +  40
-----    ------    ----    -----    -----
 -666     -3800      88      172     1028
```

## Code Overview

- **`arithmetic_arranger`**: The main function that contains all the logic for validation, formatting, calculation, and final assembly of the problem strings.
- **`main`**: An execution block that runs a comprehensive suite of test cases to demonstrate all features and error handling capabilities of the script.

## Technologies Used

- **Language:** Python 3
- **Key Concepts:** String Manipulation, F-String Formatting, Guard Clauses, Type Hinting, Docstrings
