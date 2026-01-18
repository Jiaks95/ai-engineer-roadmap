"""
File: nutrition.py
Author: Oscar Jia
Assignment: CS50P Problem Set 2: Nutrition Facts
Description: 
    Prompts the user for a fruit and outputs the number of 
    calories in one portion of that fruit, based on the 
    FDA's Poster for Raw Fruits. It utilizes dictionary 
    mapping created from zipped lists for efficient lookup.
"""

def main():
    fruits = ["Apple", "Avocado", "Banana", 
              "Cantaloupe", "Grapefruit", "Grapes", 
              "Honeydew Melon", "Kiwifruit", "Lemon",
              "Lime", "Nectarine", "Orange", "Peach", 
              "Pear", "Pineapple", "Plums", "Strawberries", 
              "Sweet Cherries", "Tangerine", "Watermelon"]
    
    calories = [130, 50, 110, 50, 60, 90, 50, 90, 15, 20, 
                60, 80, 60, 100, 50, 70, 50, 100, 50, 80]
    
    fruits_calories = dict(zip(fruits, calories))

    item = input("Item: ").strip().title()

    if item in fruits_calories:
        print(f"Calories: {fruits_calories[item]}")

main()