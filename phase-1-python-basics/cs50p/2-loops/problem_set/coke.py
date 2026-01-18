"""
File: coke.py
Author: Oscar Jia
Assignment: CS50P Problem Set 2: Coke Machine
Description: 
    Simulates a vending machine that sells Coke for 50 cents. 
    Only accepts denominations of 25, 10, and 5 cents. 
    The program tracks the amount due and informs the user 
    of any change owed once the total is reached.
"""

ACCEPTED_DENOMINATIONS = [5, 10, 25]

def main():
    
    remaining_amount = 50

    while remaining_amount > 0:
        print(f"Amount Due: {remaining_amount}")
        inserted_amount = int(input("Insert Coin: "))

        if inserted_amount not in ACCEPTED_DENOMINATIONS:
            continue

        remaining_amount -= inserted_amount

    print(f"Change Owed: {abs(remaining_amount)}")

main()