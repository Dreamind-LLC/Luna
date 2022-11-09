import battleHandler # Import Game Library
import IO # Library Model for IO Menu

def main():

    IOconsole = IO.Console()
    IOconsole.title_menu("Welcome!")

    game_options = ['New Game', 'Exit Game']
    start_game = IOconsole.menu_options(game_options)
    
    # Keep playing game until user decided to exit the program
    while start_game == 1:
        
        # Initalize the batlle object
        battle = battleHandler.battleHandler(IOconsole)
        
        # Continu the game with a random player turn until a player wins
        battle.fight()
        
        # Once game ends ask if user would like to play again
        start_game = IOconsole.menu_options(game_options)
    
    # Prompt user to exit game
    input(" Press the Enter Key to Exit.")
    IOconsole.title_menu("Goodbye!")

if __name__ == "__main__":
    main()