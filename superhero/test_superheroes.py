import unittest
from superheroes import Hero, Ability


class HeroTest(unittest.TestCase):
    
    def test_init(self):
        hero = Hero("Superman")
        assert hero.name is "Superman"
        assert hero.starting_health == 100
        assert hero.current_health == hero.starting_health
        assert hero.abilities == []

    #TODO: double check this method
    def test_add_ability(self):
        hero = Hero("Superman")
        ability1 = Ability("Speed", 200)
        assert hero.abilities.append(ability1)
        # assert hero.abilities.append("Power")
        # assert hero.abilities.append("Low IQ")
        # assert hero.abilities == ["Speed", "Power", "Low IQ"]
        assert len(hero.abilities) == 1

    def test_attack(self):
        pass

if __name__ == "__main__":
    unittest.main()
