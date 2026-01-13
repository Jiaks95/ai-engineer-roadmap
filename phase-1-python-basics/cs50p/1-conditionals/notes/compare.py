def main():
    x = int(input("What's x? "))
    y = int(input("What's y? "))

    if x < y:
        print(f"{x} is less than {y}")

    elif x > y:
        print(f"{x} is greater than {y}")

    else:
        print(f"{x} is equal to {y}")

def main_2():
    x = int(input("What's x? "))
    y = int(input("What's y? "))

    if x < y or x > y:
        print(f"{x} is not equal to {y}")

    else:
        print(f"{x} is equal to {y}")

def main_3():
    x = int(input("What's x? "))
    y = int(input("What's y? "))

    if x != y:
        print(f"{x} is not equal to {y}")

    else:
        print(f"{x} is equal to {y}")

main()
main_2()
main_2()