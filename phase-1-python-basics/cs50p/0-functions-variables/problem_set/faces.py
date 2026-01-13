def main():

    user_input = input("Write something: ")

    formatted_user_input = convert(user_input)

    print(formatted_user_input)

def convert(message):

    return message.replace(":)", "🙂").replace(":(", "🙁")

main()