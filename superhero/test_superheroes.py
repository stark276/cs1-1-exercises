import unittest
from superheroes import Hero, Ability


class HeroTest(unittest.TestCase):
    
    def test_init(self):
        hero = Hero("Superman")
        assert hero.name is "Superman"
        assert hero.starting_health == 100
        assert hero.current_health == hero.starting_health
        assert hero.abilities == []