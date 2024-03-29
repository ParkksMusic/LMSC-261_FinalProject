class Weapon:
    name = ""
    def __init__(self):
        raise NotImplementedError("Do not create raw Weapon objects.")

    def __str__(self):
        return self.name


class Rock(Weapon):
    def __init__(self):
        self.name = "Rock"
        self.description = "A fist-sized rock, suitable for bludgeoning."
        self.damage = 5
        self.value = 1


class Dagger(Weapon):
    def __init__(self):
        self.name = "Dagger"
        self.description = "An easily concealed blade. They will never see it coming."
        self.damage = 10
        self.value = 20


class RustySword(Weapon):
    def __init__(self):
        self.name = "Rusty sword"
        self.description = "Your mother told you not to leave your sword out in the rain...You didn't listen"
        self.damage = 20
        self.value = 100


class Consumable:
    def __init__(self):
        raise NotImplementedError("Do not create raw Consumable objects.")

class CookedMeat(Consumable):
    def __init__(self):
        self.name = "CookedMeat"
        self.healing_value = 10
        self.value = 12


class HealingPotion(Consumable):
    def __init__(self):
        self.name = "Healing Potion"
        self.healing_value = 50
        self.value = 60
