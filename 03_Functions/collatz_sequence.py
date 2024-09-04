import sys


def collatz(number):
    if number % 2 == 0:
        value = number // 2
    elif number % 2 == 1:
        value = 3 * number + 1

    print(value)
    return value


try:
    input = int(input("Enter number.\n"))
    while True:
        if input == 1:
            break
        else:
            input = collatz(number=input)

except:
    sys.exit()

# scoring by gpt4o
"""
Improved Exception Handling: Now it catches only ValueError for invalid input, and provides a clear message to the user.
Renamed Variable: I renamed the input variable to number to avoid shadowing the built-in input() function.
Simplified while Loop: The loop now checks directly for number != 1, making the logic cleaner.
Use of if __name__ == "__main__":: This is a common Python pattern that allows you to run code only when the file is executed directly, not when it is imported as a module.

Scoring:
Structure: 8/10 (Great start, but needs some refinement).
Error Handling: 6/10 (General exception handling is used, which should be more specific).
Readability: 9/10 (Just a small issue with using input as a variable name).
Functionality: 10/10 (It works correctly, achieving the Collatz sequence).
"""
