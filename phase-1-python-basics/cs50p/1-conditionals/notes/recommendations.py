def main():
    difficulty = input("Difficult or casual: ").strip().title()

    if difficulty not in ["Difficult", "Casual"]:
        print("Enter a valid difficulty")
        return

    players = input("Multiplayer or singleplayer: ").strip().title()

    if players not in ["Multiplayer", "Singleplayer"]:
        print("Enter a valid number of players")
        return

    if difficulty == "Difficult" and players == "Multiplayer":
        recommend("Poker")

    elif difficulty == "Difficult" and players == "Singleplayer":
        recommend("Klondike")
    
    elif difficulty == "Casual" and players == "Multiplayer":
        recommend("Hearts")

    else:
        recommend("Clock")

def recommend(game): 
    print(f"You might like {game}")

main()