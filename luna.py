import battleHandler # Import Game Library
import IO # Library Model for IO Menu

def main():
    """
    Main game menu. Will great user and ask if they woul like to 
    play a game or quit. If user selects to play, the game engine
    battlehander will be initated, otherwise the program will exit.
    """

    # Create game interface
    IOconsole = IO.Console()

    # Display main game menu
    title = "Luna and the Darkness of Magic"
    game_options = ['New Game', 'Exit Game']
    response = IOconsole.display_menu(title, game_options)
    
    # Keep playing game until user decided to exit the program
    while response == 1:
        
        # Initalize the battle handler object
        battle = battleHandler.battleHandler(IOconsole)
        
        # Continu the game with a random player turn until a player wins
        battle.fight()
        
        # Once game ends ask if user would like to play again
        title = " Would you like to play a new game?"
        response = IOconsole.display_menu(title, game_options)
    
    # Prompt user to exit game
    IOconsole.display_text(" Press the Enter Key to Exit.")
    IOconsole.display_title("Goodbye!")

if __name__ == "__main__":
    main()