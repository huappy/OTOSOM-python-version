import unittest
from battles import *


# test objects
p_1 = Player("Sasha", 100, 22, 34, 15, 16, [])
p_2 = Player("Peter", 15, 5, 3, 5, 7, [])

e_1 = Enemy("Lawrence", 120, 50, 10, 10, 8, [])
e_2 = Enemy("Blackwell", 200, 20, 15, 10, 3, [])


# run tests individually for correct results, otherwise they will interfere with each other
class MyTestCase(unittest.TestCase):

    def test_player_attack(self):
        self.assertEqual(player_attack(p_1, e_1), (12, 108), msg="Incorrect Calculation")
        self.assertEqual(player_attack(p_1, e_2), (7, 193), msg="Incorrect Calculation")
        self.assertEqual(player_attack(p_2, e_1), (0, 108), msg="Incorrect Calculation")
        self.assertEqual(player_attack(p_2, e_2), (0, 193), msg="Incorrect Calculation")

    def test_waltz_(self):
        self.assertEqual(waltz(p_1), 20, msg="Incorrect Calculation")

    def test_rhapsody(self):
        self.assertEqual(rhapsody(p_1), 100, msg="Must not go above max")      # test for max
        p_1.temp_hp -= 30
        self.assertEqual(rhapsody(p_1), 80, msg="Incorrect Calculation")       # general test

    def test_ballad(self):
        self.assertEqual(ballad(p_1), 27, msg="Incorrect Calculation")

    def test_enemy_attack(self):
        self.assertEqual(enemy_attack(p_1, e_1), (16, 84), msg="Incorrect Calculation")
        self.assertEqual(enemy_attack(p_1, e_2), (0, 84), msg="Cannot be negative")
        self.assertEqual(enemy_attack(p_2, e_1), (47, 0), msg="HP Cannot be Negative")
        self.assertEqual(enemy_attack(p_2, e_2), (17, 0), msg="Cannot be negative")


if __name__ == '__main__':
    unittest.main()
