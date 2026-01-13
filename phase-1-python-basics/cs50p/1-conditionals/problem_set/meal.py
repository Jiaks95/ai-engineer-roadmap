"""
File: meal.py
Author: Oscar Jia
Assignment: CS50P Problem Set 1: Meal Time
Description: 
    Converts 24-hour time (e.g., "7:30") to a decimal float (7.5).
    Determines if the time falls within breakfast, lunch, or dinner ranges.
"""

def main():
    time = input("What time is it? ").strip()

    time = convert(time)

    if 18 <= time <= 19:
        print("dinner time")

    elif 12 <= time <= 13:
        print("lunch time")

    elif 7 <= time <= 8:
        print("breakfast time")

    else:
        return

def convert(time):
    hour, minute = time.split(":")

    return float(hour) + float(minute) / 60


if __name__ == "__main__":
    main()