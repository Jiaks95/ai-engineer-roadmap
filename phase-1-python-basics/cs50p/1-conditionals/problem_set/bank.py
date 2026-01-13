"""
File: bank.py
Author: Oscar Jia
Assignment: CS50P Problem Set 1: Home Federal Savings Bank
Description: 
    Prompts the user for a greeting.
    Outputs "$0" if the input starts with "hello",
    "$20" if it starts with an "h" but not "hello",
    and "$100" otherwise.
    Handles case-insensitivity and whitespace.
"""

def main():
    user_greeting = input("Greeting: ").strip().lower()

    if user_greeting.startswith("hello"):
        print("$0")

    elif user_greeting.startswith("h"):
        print("$20")

    else:
        print("$100")

main()