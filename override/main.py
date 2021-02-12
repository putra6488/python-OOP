class Hero:

    def __init__(self, name,health):
        self.name = name
        self.health = health

    def showInfo(self, tipe):
        print("{} health : {}".format(self.name, self.health))

class Hero_mage(Hero):
    
    def __init__(self, name):
        super().__init__(name, 100)
    
    def showInfo(self):
        print("{} \n\t Tipe : Mage, \n\t health : {}".format(self.name, self.health))

class Hero_tank(Hero):
    
    def __init__(self, name):
        super().__init__(name, 300)



kagura = Hero_mage("Kagura")
lolita = Hero_tank("Lolita")

kagura.showInfo()
