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
        self.current_health = current_health
        self.abilities = list()

    def add_ability(self, ability):
        ''' Add ability to abilities list '''
        return abilities.append(ability)

    def attack(self):
        '''
        Calculates damage from list of abilities.
        This method should call Ability.attack()
        on every ability in self.abilities and
        return the total.
        '''
        total = 0
        for ability in self.abilities:
            ability.attack()
            total += 1
        return total


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
        # if self.abilities is None or opponent.abilities is None:
        # while self.current_health != 0 or opponent.current_health != 0:
            # self.attack(opponent)
        print("{} vs {}. FIGHT!".format(self.name, opponent.name)
        if self.abilities is None and opponent.abilities is None:
            self.take_damage(0)
            opponent.take_damage(0)
            print("Both heroes don't have abilities")
        else:
            while self.is_alive is True and opponent.is_alive is True:
                self.take_damage(opponent.attack())
                opponent.take_damage(self.attack())
                if self.is_alive is False:
                    print("{} won!".format(opponent.name))
                else:
                    print("{} won!".format(self.name))

class Ability:
    def __init__(self, name, max_damage):
        '''
        Initialize the values passed into this
        method as instance variables.
         '''
        pass

    def attack(self):
        '''
        Return a random attack value
        between 0 and max_damage.
        '''
        pass


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    pass