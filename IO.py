class Console(object):
    """
    The Console class is a simple input output helper to help
    faciliate a simple consistent interface for the player.
    """

    def __init__(self, window_length=96, padding=2):
        self.window_length = window_length
        self.padding = padding
        self.padding_diff = window_length - padding
        self.default_prompt = " Input: "

    # String formatting methods
    def string_format_center(self, string):
        return string.center(self.padding_diff, " ")

    def string_format_left(self, string):
        return string.ljust(self.padding_diff, " ")

    def string_format_right(self, string):
        return string.rjust(self.padding_diff, " ")

    def string_format_edge(self, string):
        return "|" + string + "|"

    # Display input prompt
    def display_input(self, prompt=None):
        if prompt == None:
            prompt = self.default_prompt
        return input(prompt)

    # Display text in game console
    def display_text(self, prompt, orientation='left', edge=False):

        # Align string 
        if orientation == 'left':
            prompt = self.string_format_left(prompt)
        elif orientation == 'center':
            prompt = self.string_format_center(prompt)
        elif orientation == 'right':
            prompt = self.string_format_right(prompt)

        # Add edge to string
        if edge == True:
            prompt = self.string_format_edge(prompt)

        print(prompt)

    # Display title in game console
    def display_title(self, string, padding=2):
        print(self.window_length*"=")
        self.display_text(string, orientation='center', edge=True)
        print(self.window_length*"=")

    # Display list of menu options
    def display_menu_options(self, options_list):
        for option in range(len(options_list)):
            option_str = " [{}]: {}".format(option+1, options_list[option])
            option_str = self.string_format_left(option_str)
            print(option_str)

    # Display menu
    def display_menu(self, menu_title, menu_options=None, prompt=None, err_msg=" Invalid Response"):
        
        # Set variables
        valid_input = False
        response = None
        err_message = self.string_format_left(err_msg)
        min_response = 0
        max_response = None

        # Update max_response range based on if menu is a list 
        if type(menu_options) == list:
            max_response = len(menu_options)
        elif type(menu_options) == int:
            max_response = menu_options
        
        # While the input is not a valid input repeat the prompt
        while (valid_input==False):

            # Display menu title
            self.display_title(menu_title)

            # If menu is multiple choice
            if type(menu_options) == list:

                # Display menu options
                self.display_menu_options(menu_options)

            # Try to get user input
            try:
                response = int(self.display_input(prompt))
                
            # Display error if unable to process input
            except:
                print(err_message)
                continue

            # Determine if response is valid
            else:
                # Determine if response is in option range
                if response > min_response and response <= max_response:
                    valid_input = True
                    
                # Otherwise display error
                else:
                    print(err_message)
                    continue

        # Return response        
        return response

    # Display player and its attributes
    def display_player_attributes(self, att_list):

        # Determine spacing between cells
        cell_size = self.window_length/len(att_list)
        row = "|"

        # For each attribute
        for att in att_list:

            # If attribute is a number, round to 2 decimals
            if isinstance(att, int) or isinstance(att, float):
                att = "{:.2f}".format(att)

            # Format - center string and place border
            row += att.center(int(cell_size-1), " ")
            row += "|"

        # Display entire row to console and print bottom border
        print(row)
        print(self.window_length*"-")

    # Display team stats
    def display_team_stats(self, team):

        # For each player
        for team_member in team.get_teammembers():

            # Get individual player stats
            player = team.get_teammember(team_member)
            player_attr = player.get_all_attr()

            # display player's stats
            self.display_player_attributes(player_attr)

    
    # Display game status to user
    def display_battle_stats(self, heroes, enemies):

        # List of player attributes
        att_list = ['name', 'health', 'mana', 'speed', 'accuracy']
        
        # Enemy Stats 
        self.display_title("Enemy Stats")
        self.display_player_attributes(att_list)

        # Display enemy stats
        self.display_team_stats(enemies)

        # Hero stats
        self.display_title("Hero Stats")
        self.display_player_attributes(att_list)

        # Display hero stats
        self.display_team_stats(heroes)

    # Display who is current active player
    def display_active_player(self, active_player):
        active_player_string = " {}'s turn".format(active_player.get_name())
        self.display_title(active_player_string)
