class Console(object):

    def __init__(self, window_length=96, padding=2):
        self.window_length = window_length
        self.padding = padding
        self.padding_diff = window_length - padding

    # String Formatting Methods
    def string_format_center(self, string):
        return string.center(self.padding_diff, " ")

    def string_format_left(self, string):
        return string.ljust(self.padding_diff, " ")

    def string_format_right(self, string):
        return string.rjust(self.padding_diff, " ")

    def string_format_edge(self, string):
        return "|" + string + "|"       

    # Display Formatting Methods
    def display_text(self, prompt, orientation='left'):
        if orientation == 'left':
            prompt = self.string_format_left(prompt)
        elif orientation == 'center':
            prompt = self.string_format_center(prompt)
        elif orientation == 'right':
            prompt = self.string_format_right(prompt)
        return self.string_format_edge(prompt)

    def display_title(self, string, padding=2):
        print(self.window_length*"=")
        string = self.display_text(string, orientation='center')
        print(string)
        print(self.window_length*"=")

    def display_menu_options(self, options_list):
        for option in range(len(options_list)):
            option_str = " [{}]: {}".format(option+1, options_list[option])
            option_str = self.string_format_left(option_str)
            print(option_str)

    # Valid Response
    def display_menu(self, menu_title, menu_options=None, prompt=" Input: ", err_msg=" Invalid Response"):
        
        valid_input = False
        response = None
        
        # While the input is not a valid input repeat the prompt
        while (valid_input==False):

            self.display_title(menu_title)

            if menu_options:
                self.display_menu_options(menu_options)

            err_message = self.string_format_left(err_msg)

            try:
                response = int(input(prompt))
            except:
                print(self.string_format_edge(err_message))
                continue
            else:
                if response >= 1 and response <= len(menu_options):
                    valid_input = True
                else:
                    print(self.string_format_edge(err_message))
                    continue

        # Return response        
        return response

    def display_player_attributes(self, att_list):
        cell_size = self.window_length/len(att_list)
        row = "|"
        for att in att_list:
            if isinstance(att, int) or isinstance(att, float):
                att = "{:.2f}".format(att)
            row += att.center(int(cell_size-1), " ")
            row += "|"
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
    def display_battle_stats(self, active_player, heroes, enemies):

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
        active_player_string = " {}'s turn".format(active_player.get_name())
        self.display_title(active_player_string)
