import numpy as np
import skills as sk

class skillstree(object):
    def __init__(self, user):
        self.user = user
        self.skills = {}
        self.default_skills()
        
    def default_skills(self):
        self.learn(sk.Bash(self.user))
        self.learn(sk.FireBlast(self.user))
        self.learn(sk.IceBlast(self.user))
        self.learn(sk.LightingBolt(self.user))
        self.learn(sk.Venom(self.user))
        self.learn(sk.Healing(self.user))
        #self.learn(sk.ManaShield(self.user))
    
    def learn(self, skill):
        self.skills[skill.get_name()] = skill
        
    def get_skills(self):
        return self.skills
    
    def get_skills_options(self):
        options = []
        for skill in self.get_skills().values():
            for target in skill.get_target_options().values():
                options.append((skill, target))
        return options
    
    def get_skill(self, skill):
        if skill in self.skills:
            return self.skills[skill]
        else:
            print('Skill does not exist!')
            
    def display(self):
        print("---------------------------------------------------")
        print("{}'s Skills:".format(self.user.get_name()))
        skills_list = list(self.skills.keys())
        menu_index = 1
        for skill in skills_list:
            print("[{}] ".format(menu_index) + skill + " ")
            menu_index += 1
        print("[{}] ".format(menu_index) + "Return to main player menu")
        print("---------------------------------------------------")
        
    def interface(self):
        
        # Display skills
        self.display()
    
        # Initialize choice variable to determine what skill to use
        choice = 0
        
        # Let user select an item or exit menu
        while (choice < 1 or choice > (len(self.skills)+1)):
            try:
                choice = int(input("Select a skill or return back to main player option menu: "))
            except:
                print("Invalid Response")
                continue
        
        # Quit skills menu
        if choice == len(self.skills)+1:
            return None
        
        else:
            # Select skill
            skill_list = list(self.skills.keys())
            skill_name = skill_list[choice-1]
        
            # Display skill selected
            print("{} was selected!".format(skill_name))
        
            return self.skills[skill_name]

    
    