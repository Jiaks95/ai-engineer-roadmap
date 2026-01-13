def main():
    x = int(input("What's x: "))

    if is_even(x):
        print(f"{x} is even")
    
    else:
        print(f"{x} is odd")

def is_even(number):
    # return True if number % 2 == 0 else False
    return number % 2 == 0

main()