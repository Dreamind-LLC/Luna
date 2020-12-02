import battleHandler # Import Game Library

def main():
    print("\n\t\tWelcome!")

    start_game = valid_input()
    
    # Keep playing game until user decided to exit the program
    while start_game == 1:
        
        # Initalize the batlle object
        battle = battleHandler.battleHandler()
        
        # Continu the game with a random player turn until a player wins
        battle.fight()
        
        # Once game ends ask if user would like to play again
        start_game = valid_input()
    
    # Prompt user to exit game
    input("Press the Enter Key to Exit.")
    
def valid_input():
    
    # Give player options
    option = None
    valid_input = False
        
    # Keep prompting user for a valid option 
    while (valid_input==False):
        try:
            print("[1]: New Game\n[2]: Exit Game")
            option = int(input("Input: "))
        except:
            print("Invalid Response")
            continue
        else:
            # Valid response
            if (option == 1) or (option == 2):
                valid_input = True
            else:
                print("Invalid Response")
                continue
    
    return option


if __name__ == "__main__":
    main()