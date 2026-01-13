def main():
    # Ask user for their name
    name = input("Enter your name: ")
    # Greet the user
    print(f"Hello, {name}. Welcome to machine learning!")
    print("Hello", end=", ")
    print(name)
    print("Hello, \"friend\"")

    name_with_whitespace = input("Enter your name with extra spaces: ")

    name_stripped = name_with_whitespace.strip()

    name_titled = name_stripped.title()
    print(f"Hello, {name_titled}. Welcome to machine learning!")

    formatted_name = input("Enter your name: ").strip().title()
    print(f"Hello, {formatted_name}. Welcome to machine learning!")

if __name__ == "__main__":
    main()