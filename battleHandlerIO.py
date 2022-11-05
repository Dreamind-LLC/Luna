class BattleHanderIO(object):
    
    def welcome_message(self):
        # Begin Game Message
        #print("\n===================================================")
        #print("||                    Begin Game                 ||")
        #print("===================================================\n")
        print("\n")
        padding_num = 60
        print(padding_num*" ")
        string = "Begin Game "
        string = string.center((padding_num-len(string)-2*" "))
        string = "|" + string + "|"
        print(padding_num*" ")
        
    def game_over_message(self):
        # Display "Game Over" Sign
        #print("\n===================================================")
        #print("||                    Game Over                  ||")
        #print("===================================================\n")
        print("\n")
        padding_num = 60
        print(padding_num*" ")
        string = "Game Over "
        string = string.center((padding_num-len(string)-2*" "))
        string = "|" + string + "|"
        print(padding_num*" ")
            
    # Prompt user to exit (y/n)
    def ask_yes_no(self, question):
        response = None
        while response not in ("y", "n"):
            response = input(question).lower()
        return response
    
    # Display game status to user
    def battle_stats(self, active_player, heroes, enemies):
        
        # Display which player is taking a turn
        print("===================================================")
        print("| {}'s turn:".format(active_player.get_name()))
        
        # Print hero stats
        print("===================================================")
        print("|\t\tHero Stats\t|")
        print("---------------------------------------------------")
        hero_name = "|\tName\t|\t"
        hero_health = "|\tHealth\t|\t"
        hero_health_list = []
        hero_mana = "|\tMana\t|\t"
        hero_mana_list = []
        
        # For each hero get the name, health, and mana
        for player in heroes.get_teammembers():
                hero = heroes.get_teammember(player)
                hero_name += hero.get_name() + "\t|\t"
                hero_health += "{:.2f}" + "\t|\t"
                hero_health_list.append(hero.get_health())
                hero_mana += "{:.2f}" + "\t|\t"
                hero_mana_list.append(hero.get_mana())
                
        # Display stats
        print(hero_name)
        print("---------------------------------------------------")
        print(hero_health.format(*hero_health_list))
        print("---------------------------------------------------")
        print(hero_mana.format(*hero_mana_list))
        
        # Print enemy stats
        print("===================================================")
        print("|\t\tEnemy Stats\t|")
        print("---------------------------------------------------")
        enemy_name = "|\tName\t|\t"
        enemy_health = "|\tHealth\t|\t"
        enemy_health_list = []
        enemy_mana = "|\tMana\t|\t"
        enemy_mana_list = []
        
        # For each enemy get the name and health
        for player in enemies.get_teammembers():
                enemy = enemies.get_teammember(player)
                enemy_name += enemy.get_name() + "\t|\t"
                enemy_health += "{:.2f}" + "\t|\t"
                enemy_health_list.append(enemy.get_health())
                enemy_mana += "{:.2f}" + "\t|\t"
                enemy_mana_list.append(enemy.get_mana())
                
        # Display stats
        print(enemy_name)
        print("---------------------------------------------------")
        print(enemy_health.format(*enemy_health_list))
        print("---------------------------------------------------")
        print(enemy_mana.format(*enemy_mana_list))
        print("===================================================")