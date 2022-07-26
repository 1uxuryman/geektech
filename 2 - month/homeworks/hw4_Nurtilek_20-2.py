import random
from enum import Enum


class SuperAbility(Enum):
    CRITICAL_DAMAGE = 1
    HEAL = 2
    BOOST = 3
    SAVE_DAMAGE_AND_REVERT = 4
    REVERT_HEALTH = 5
    BOSS_OFF = 6
    SIZE_ON = 7
    REVIVAL = 8


class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f'{self.__name} health: {self.__health} damage: {self.__damage}'


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super(Boss, self).__init__(name, health, damage)
        self.__defence = None

    @property
    def defence(self):
        return self.__defence

    def choose_defence(self, heroes):
        selected_hero = random.choice(heroes)
        self.__defence = selected_hero.super_ability

    def hit(self, heroes):
        for hero in heroes:
            if hero.health > 0:
                hero.health = hero.health - self.damage

    def __str__(self):
        return "BOSS " + super(Boss, self).__str__() + f" defence: {self.__defence}"


class Hero(GameEntity):
    def __init__(self, name, health, damage, super_ability):
        super(Hero, self).__init__(name, health, damage)
        self.__super_ability = super_ability

    @property
    def super_ability(self):
        return self.__super_ability

    def hit(self, boss):
        if boss.health > 0 and self.health > 0 and self.__super_ability != boss.defence:
            boss.health = boss.health - self.damage

    def apply_super_power(self, boss, heroes):
        pass


class Hacker(Hero):
    def __init__(self, name, health, damage):
        super(Hacker, self).__init__(name, health, damage, SuperAbility.REVERT_HEALTH)

    def apply_super_power(self, boss, heroes):
        hp = random.randint(10, 21)
        print(f'hp of revert: {hp}')
        for hero in heroes:
            boss.health -= hp
            hero.health += hp


class Thor(Hero):
    def __init__(self, name, health, damage):
        super(Thor, self).__init__(name, health, damage, SuperAbility.BOSS_OFF)

    def apply_super_ability(self, boss):
        off = 0
        if self.health > 0 and round_number == 1:
            self.damage = off
        elif self.damage == off:
            boss.damage = 50
        else:
            boss.damage = 0


class AntMan(Hero):
    def __init__(self, name, health, damage):
        super(AntMan, self).__init__(name, health, damage, SuperAbility.SIZE_ON)

    def apply_super_power(self, boss, heroes):
        rnd = random.randint(1, 5)
        if rnd == 5:
            self.health += 150
            self.damage += 8
            print("+ Size")
        elif rnd == 1 or 2 or 3 or 4:
            self.health -= 150
            self.damage -= 3
            print(" - Size")


class Wither(Hero):
    def __init__(self, name, health, damage):
        super(Wither, self).__init__(name, health, damage, SuperAbility.REVIVAL)

    def apply_super_ability(self, heroes):
        self.damage = 0
        for hero in heroes:
            if hero.health >= 0:
                self.health = hero.health


class Warrior(Hero):

    def __init__(self, name, health, damage):
        super(Warrior, self).__init__(name, health, damage, SuperAbility.CRITICAL_DAMAGE)

    def apply_super_power(self, boss, heroes):
        coeff = random.randint(2, 5)
        print(f"Coefficient of Critical: {coeff}")
        boss.health -= self.damage * coeff


class Magic(Hero):
    def __init__(self, name, health, damage):
        super(Magic, self).__init__(name, health, damage, SuperAbility.BOOST)

    def apply_super_power(self, boss, heroes):
        boost_points = random.randint(5, 11)
        print(f"Boost: {boost_points}")
        for hero in heroes:
            if hero != self and hero.health > 0 and hero.super_ability != SuperAbility.CRITICAL_DAMAGE:
                hero.damage += boost_points


class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        super(Medic, self).__init__(name, health, damage, SuperAbility.HEAL)
        self.__heal_points = heal_points

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if self != hero and hero.health > 0:  # self.name != hero.name
                hero.health += self.__heal_points


class Berserk(Hero):
    def __init__(self, name, health, damage):
        super(Berserk, self).__init__(name, health, damage, SuperAbility.SAVE_DAMAGE_AND_REVERT)
        self.__saved_damage = 0


round_number = 0


def is_game_finished(boss, heroes):
    if boss.health <= 0:
        print("Heroes won!!!")
        return True
    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break
    if all_heroes_dead:
        print("Boss won!!!")
    return all_heroes_dead


def print_statistics(boss, heroes):
    print("ROUND " + str(round_number) + " -----------------")
    print(boss)
    for hero in heroes:
        print(hero)


def play_round(boss, heroes):
    global round_number
    round_number += 1
    boss.choose_defence(heroes)
    boss.hit(heroes)
    for hero in heroes:
        if hero.health > 0 and hero.super_ability != boss.defence:
            hero.hit(boss)
            hero.apply_super_power(boss, heroes)
    print_statistics(boss, heroes)


def start_game():
    boss = Boss("Rashan", 2000, 50)
    warrior = Warrior("Hunter", 220, 10)
    doc = Medic("Oracle", 200, 5, 15)
    magic = Magic("Naruto", 230, 20)
    berserk = Berserk("Axe", 210, 15)
    assistant = Medic("Dasemond", 240, 10, 5)
    hacker = Hacker("Comander X", 150, 5)
    thor = Thor("Thor", 180, 10)
    ant = AntMan("AntMan", 150, 10)
    wit = Wither("Witcher", 200, 0)

    heroes = [warrior, doc, magic, berserk, assistant, hacker, thor, ant, wit]

    print_statistics(boss, heroes)

    while not is_game_finished(boss, heroes):
        play_round(boss, heroes)


start_game()
