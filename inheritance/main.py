# super class
class Hero:

    def __init__(self,name,health):
        self.name = name
        self.health = health

# sub class
class Hero_mage(Hero):
    pass

# sub class
class Hero_tank(Hero):
    pass

kagura = Hero("Kagura", 100)
cecilion = Hero_mage('Cecilion', 100)
lolita = Hero_tank("Lolita", 200)

print(kagura.name)
print(cecilion.name)
print(lolita.name)