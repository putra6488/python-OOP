class Hero:

    def __init__(self, name, health):
        self.name = name
        self.health = health

    def showInfo(self):
        print("{} dengan health : {}".format(self.name, self.health))

class Hero_mage(Hero):
    def __init__(self,name):
        # Hero.__init__(self,name, 100)
        # ambil method super class
        super().__init__(name, 100)
        # ambil method showinfo di super class
        super().showInfo()

class Hero_tank(Hero):
    def __init__(self,name):
        super().__init__(name, 300)
        super().showInfo()


kagura = Hero_mage("Kagura")
lolita = Hero_tank("Lolita")

print(20*"=")
print(kagura.name , " ", kagura.health)
print(lolita.name , " ", lolita.health)