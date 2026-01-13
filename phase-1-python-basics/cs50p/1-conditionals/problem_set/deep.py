"""
File: deep.py
Author: Oscar Jia
Assignment: CS50P Problem Set 1: Deep Thought
Description: 
    Prompts the user for the answer to the Great Question of Life.
    Outputs "Yes" if the input is 42 (numeric or text), otherwise "No".
    Handles case-insensitivity and whitespace.
"""

def main():
    user_answer = input("What is the Answer to the Great Question of Life, the Universe and Everything? ").strip().lower()

    match user_answer:
        case "42" | "forty-two" | "forty two":
            print("Yes")

        case _:
            print("No")

main()