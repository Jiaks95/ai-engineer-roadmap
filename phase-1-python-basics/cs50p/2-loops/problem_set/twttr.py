"""
File: twttr.py
Author: Oscar Jia
Assignment: CS50P Problem Set 2: Just setting up my twttr
Description: 
    Prompts the user for a string of text and then outputs 
    that same text but with all vowels (A, E, I, O, and U) 
    omitted, regardless of whether they were entered in 
    uppercase or lowercase.
"""

VOWELS = {"a", "e", "i", "o", "u"}

def main():
    user_input = input("Input: ").strip()

    print("Output: ", end="")


    for char in user_input:
        if char.lower() in VOWELS:
            continue

        print(char, end="")

    print()

main()