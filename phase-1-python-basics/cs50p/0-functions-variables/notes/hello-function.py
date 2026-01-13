def main():

    # Ask user for their name, remove withespaces from the str and capitalize the first letter of each word
    name = input("What's your full name: ").strip().title()

    if " " not in name:

        # Output with the user's name
        hello(name)

    else:    
        first_name, last_name = name.split(" ")

        # Output with the user's name
        hello(first_name)
        
        # Output with the user's surname
        hello(last_name)

    #Output without passing the user's name
    hello()

# Function to print greeting to user
def hello(to="World"):
    print(f"Hello, {to}!")

main()

def main_2():

    # Ask user for a number to get it's square
    x = int(input("Enter a number to get it's square: "))

    # Print x squared
    print(f"{x} squared is {square(x)}")

# Function to get the square of a number n
def square(n):
    return n * n

main_2()