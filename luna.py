import battleHandler # Import Game Library
import IO # Library Model for IO Menu

def main():

    # Create game interface
    IOconsole = IO.Console()

    # Display main game menu
    title = "Luna and the Darkness of Magic"
    game_options = ['New Game', 'Exit Game']
    response = IOconsole.display_menu(title, game_options)
    
    # Keep playing game until user decided to exit the program
    while response == 1:
        
        # Initalize the batlle object
        battle = battleHandler.battleHandler(IOconsole)
        
        # Continu the game with a random player turn until a player wins
        battle.fight()
        
        # Once game ends ask if user would like to play again
        title = " Would you like to play a new game?"
        response = IOconsole.display_menu(title, game_options)
    
    # Prompt user to exit game
    IOconsole.display_text("Press the Enter Key to Exit.")
    IOconsole.display_title("Goodbye!")

if __name__ == "__main__":
    main()