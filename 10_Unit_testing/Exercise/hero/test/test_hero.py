from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):
    def setUp(self):
        self.hero = Hero("name", 23, 100, 50)

    def test_constructor_hero(self):
        self.assertEqual("name", self.hero.username)
        self.assertEqual(23, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(50, self.hero.damage)

    def test_battle_with_same_names_raises(self):
        enemy = Hero("name", 25, 80, 30)
        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_with_hero_health_lower_or_equal_to_zero_raises(self):
        with self.assertRaises(ValueError) as ex:
            hero = Hero("name", 30, 0, 50)
            enemy = Hero("enemy_name", 30, 40, 60)
            hero.battle(enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_with_enemy_health_lower_or_equal_to_zero_raises(self):
        with self.assertRaises(ValueError) as ex:
            hero = Hero("name", 30, 10, 50)
            enemy = Hero("enemy_name", 30, 0, 60)
            hero.battle(enemy)
        self.assertEqual("You cannot fight enemy_name. He needs to rest", str(ex.exception))

    def test_battle_draw(self):
        hero = Hero("hero", 10, 100, 10)
        enemy = Hero("enemy", 10, 100, 10)
        result = hero.battle(enemy)
        self.assertEqual(0, hero.health)
        self.assertEqual(0, enemy.health)
        self.assertEqual(result, "Draw")

    def test_battle_when_is_not_draw_and_hero_win(self):
        hero = Hero("hero", 10, 100, 10)
        enemy = Hero("enemy", 5, 100, 5)
        result = hero.battle(enemy)
        self.assertEqual(80, hero.health)
        self.assertEqual(11, hero.level)
        self.assertEqual(15, hero.damage)
        self.assertEqual(0, enemy.health)
        self.assertEqual(result, "You win")

    def test_battle_when_is_not_draw_and_enemy_win(self):
        hero = Hero("hero", 5, 100, 5)
        enemy = Hero("enemy", 10, 100, 10)
        result = hero.battle(enemy)
        self.assertEqual(80, enemy.health)
        self.assertEqual(11, enemy.level)
        self.assertEqual(15, enemy.damage)
        self.assertEqual(0, hero.health)
        self.assertEqual(result, "You lose")

    def test_str_method(self):
        result = str(self.hero)
        self.assertEqual(f"Hero name: 23 lvl\nHealth: 100\nDamage: 50\n", result)


if __name__ == "__main__":
    main()
