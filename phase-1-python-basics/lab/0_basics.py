def main():
    user_data = {
        "id": 101,
        "name": "Alice",
        "preferences": {
            "theme": "dark",
            "notifications": True,
            "language": "es"
        }
    }

    get_theme(user_data)
    greeting(user_data)

def get_theme(data):
    theme = data["preferences"]["theme"] 
    # TODO: 1. Print the value of 'theme' (should be 'dark')
    print(f"Theme: {theme.title()}")

def greeting(data):
    user_name = data["name"]
    # TODO: 2. If language is 'es', print 'Hola Alice!', otherwise print 'Hello Alice!'
    if data["preferences"]["language"] == "es":
        print(f"Hola {user_name}!")

    else:
        print(f"Hello {user_name}!") 

if __name__ == "__main__":
    main()