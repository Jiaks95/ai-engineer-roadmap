"""
File: plates.py
Author: Oscar Jia
Assignment: CS50P Problem Set 2: Vanity Plates
Description: 
    Implements a modular validation system for vanity plates. 
    Checks length, starting characters, numeric placement, 
    and alphanumeric constraints using a series of 
    independent validation functions.
"""

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    validations = [check_length, start_with_2_letters, numbers_at_the_end, not_special_characters]

    for validation in validations:
        if not validation(s):
            return False
        
    return True

def start_with_2_letters(s):
    return s[0].isalpha() and s[1].isalpha()
    
def check_length(s):
    return len(s) >= 2 and len(s) <= 6 

def numbers_at_the_end(s):
    number = ""
    for char in s:
        if number and not char.isdigit():
            return False
        
        if char.isdigit() and not number:
            if char == "0":
                return False

            number += char
    
    return True

def not_special_characters(s):
    return s.isalnum()
        
main()