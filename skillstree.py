import numpy as np
import skills as sk
import IO

class skillstree(object):
    """
    The skillstree class is a data structure that keeps track of all
    the skills that an individual player currently has.
    """

    def __init__(self, console, user):
        self.IOconsole = console
        self.user = user
        self.skills = {}
        self.default_skills()
    
    # Add list of skills to skills tree
    def default_skills(self):
        self.learn(sk.Bash(console=self.IOconsole, user=self.user))
        self.learn(sk.FireBlast(console=self.IOconsole, user=self.user))
        self.learn(sk.IceBlast(console=self.IOconsole, user=self.user))
        self.learn(sk.LightingBolt(console=self.IOconsole, user=self.user))
        self.learn(sk.Venom(console=self.IOconsole, user=self.user))
        self.learn(sk.Healing(console=self.IOconsole, user=self.user))
    
    # Add individula skill to skills tree
    def learn(self, skill):
        self.skills[skill.get_name()] = skill
        
    # Get list of all skills
    def get_skills(self):
        return self.skills
    
    # Get list of options for each skills
    def get_skills_options(self):

        # List of available actions
        options = []

        # For each skill in skills tree
        for skill in self.get_skills().values():

            # For each available target from skill
            for target in skill.get_target_options().values():

                # Update list of actions
                options.append((skill, target))

        # Return available action list
        return options
    
    # Get skill
    def get_skill(self, skill):

        # If skill available return it
        if skill in self.skills:
            return self.skills[skill]

        # Else notify user skill does not exist
        else:
            msg = ' Skill does not exist!'
            self.IOconsole.display_input(msg)
        
    # Player's skills tree interface to select from available skills
    def interface(self):
        
        # Display Skills tree menu
        title = " {}'s Skills:".format(self.user.get_name())
        options = list(self.skills.keys())
        options.append("Return to main player menu")
        choice = self.IOconsole.display_menu(title, options)
        
        # Quit skills menu
        if choice == len(self.skills)+1:
            return None
        
        # Select skill
        else:
            # Display skill selected
            skill_list = list(self.skills.keys())
            skill_name = skill_list[choice-1]
            text = " {} was selected!".format(skill_name)
            self.IOconsole.display_text(text)
        
            return self.skills[skill_name]
