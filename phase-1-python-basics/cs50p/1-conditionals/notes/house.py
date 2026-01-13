def main():
    name = input("What's your name: ").strip().title()

    match name:
        case "Harry" | "Hermione" | "Ron": 
            print("Gryffindor")
        
        case "Draco":
            print("Slytherin")

        case _:
            print("Who?")

main()