"""
File: camel.py
Author: Oscar Jia
Assignment: CS50P Problem Set 2: camelCase
Description: 
    Prompts the user for a string in camelCase and converts it 
    into snake_case. It iterates through the input, identifying 
    uppercase letters to insert underscores and convert the 
    entire string to lowercase.
"""

def main():
    camel_case = input("camelCase: ").strip()

    snake_case = ""

    for char in camel_case:
        if char.isupper():
            snake_case += "_" + char

        else:
            snake_case += char

    print(f"snake_case: {snake_case.lower()}")

main()