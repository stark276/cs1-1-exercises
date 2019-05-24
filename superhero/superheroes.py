import random

class Hero:
    def __init__(self, name, starting_health=100):
        '''
        Initialize these values as instance variables:
        (Some of these values are passed in above, others will need to be set at a starting value.)
        abilities:List
        name:
        starting_health:
        current_health:
        '''
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = list()

    def add_ability(self, ability):
        ''' Add ability to abilities list '''
        self.abilities.append(ability)

    def attack(self):
        '''
        Calculates damage from list of abilities.
        This method should call Ability.attack()
        on every ability in self.abilities and
        return the total.
        '''
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage


    def take_damage(self, damage):
        '''
        This method should update self.current_health
        with the damage that is passed in.
        '''
        self.current_health -= damage
        return self.current_health

    def is_alive(self):  
        '''
        This function will
        return true if the hero is alive
        or false if they are not.
        '''
        if self.current_health > 0:
            return True
        else:
            return False

    def fight(self, opponent):  
        '''
        Runs a loop to attack the opponent until someone dies.
        '''
        print("{} vs {}. FIGHT!".format(self.name, opponent.name))
        # if self.abilities == 0 and opponent.abilities == 0:
        #     print("here1")
        #     self.take_damage(0)
        #     opponent.take_damage(0)
        #     print("Both heroes don't have abilities")
        # else:
        print("here1")
        while (self.is_alive is True and opponent.is_alive is True):
            print("here2")
            self.take_damage(opponent.attack())
            opponent.take_damage(self.attack())
            if self.is_alive is False:
                print("{} killed {}!".format(opponent.name, self.name))
            elif opponent.is_alive is False:
                print("{} killed {}!".format(self.name, opponent.name))

class Ability:
    def __init__(self, name, attack_strength):
        '''
        Initialize the values passed into this
        method as instance variables.
         '''
        self.name = name
        self.attack_strength = attack_strength

    def attack(self):
        '''
       Use random.randint(a, b) to select a random attack value.
        Return an attack value between 0 and the full attack.
        '''
        attack_value = random.randint(0, self.attack_strength)
        return attack_value


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero = Hero("Wonder Woman")
    print(hero.attack())
    ability = Ability("Divine Speed", 20)
    hero.add_ability(ability)
    print(hero.attack())
    new_ability = Ability("Super Human Strength", 30)
    hero.add_ability(new_ability)
    print(hero.attack())
    hero2 = Hero("Jodie Foster")
    ability2 = Ability("Science", 800)
    hero2.add_ability(ability2)
    hero.fight(hero2)