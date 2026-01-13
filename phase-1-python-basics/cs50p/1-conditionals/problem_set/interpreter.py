"""
File: interpreter.py
Author: Oscar Jia
Assignment: CS50P Problem Set 1: Math Interpreter
Description: 
    Prompts the user for an arithmetic expression (e.g., 1 + 1).
    Calculates and outputs the result formatted to one decimal place.
    Supports +, -, *, and / operations.
"""

def main():
    arithmetic_expression = input("Expression: ").strip()

    # Note: The problem spec guarantees exactly one space delimiter
    # In production, I would use .split() to handle multiple spaces between x, y and z
    x, y, z = arithmetic_expression.split(" ")

    x, z = float(x), float(z)

    result = None

    match y:
        case "+":
            result = x + z

        case "-":
            result = x - z

        case "*":
            result = x * z

        # The problem spec also guarantees that if 'y' is '/', then 'z' won't be '0'
        case "/":
            result = x / z

    print(f"{result:.1f}")

main()