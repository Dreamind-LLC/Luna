class Console(object):

    def __init__(self, window_length=96):
        self.window_length = window_length
    
    def title_menu(self, string, padding=2):
        print(self.window_length*"=")
        padding_diff = self.window_length - padding
        string = string.center(padding_diff, " ")
        string = "|" + string + "|"
        print(string)
        print(self.window_length*"=")

    def player_attributes_row(self, att_list):
        cell_size = self.window_length/len(att_list)
        row = "|"
        for att in att_list:
            if isinstance(att, int) or isinstance(att, float):
                att = "{:.2f}".format(att)
            row += att.center(int(cell_size-1), " ")
            row += "|"
        print(row)
        print(self.window_length*"-")
            
    # Prompt user to exit (y/n)
    def ask_yes_no(self, question):
        response = None
        while response not in ("y", "n"):
            response = input(question).lower()
        return response

    def display_options(self, options_list):
        for num in range(len(options_list)):
            print(" [{}]: {}".format(num+1, options_list[num]))

    # Menu options
    def menu_options(self, options_list):
        
        # set default variables
        option = None
        valid_input = False
            
        # Keep prompting user for a valid option 
        while (valid_input==False):
            self.display_options(options_list)
            try:
                option = int(input(" Input: "))
            except:
                print(" Invalid Response")
                continue
            else:
                # Valid response
                if (option == 1) or (option == 2):
                    valid_input = True
                else:
                    print(" Invalid Response")
                    continue
        return option

    # Display team stats
    def team_stats(self, team):

        # For each player
        for team_member in team.get_teammembers():

            # Get individual player stats
            player = team.get_teammember(team_member)
            player_attr = player.get_all_attr()

            # display player's stats
            self.player_attributes_row(player_attr)

    
    # Display game status to user
    def battle_stats(self, active_player, heroes, enemies):

        # List of player attributes
        att_list = ['name', 'health', 'mana', 'speed', 'accuracy']
        
        # Enemy Stats 
        self.title_menu("Enemy Stats")
        self.player_attributes_row(att_list)

        # Display enemy stats
        self.team_stats(enemies)

        # Hero stats
        self.title_menu("Hero Stats")
        self.player_attributes_row(att_list)

        # Display hero stats
        self.team_stats(heroes)

        # Display who is current active player
        active_player_string = " {}'s turn".format(active_player.get_name())
        self.title_menu(active_player_string)
