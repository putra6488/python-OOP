class Hero:
    jumlah_hero = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah_hero += 1

    # method tanpa return, tanpa aragumen
    def siapa(self):
        print("namaku : " + self.name)

    # method dengan argument, tanpa return
    def healthUp(self, up):
        self.health += up

    # method denga return
    def getHealth(self):
        return self.health

hero1 = Hero("Miya", 100, 250, 300)
hero2 = Hero("Layla", 200, 200, 200)

hero1.siapa()
hero1.healthUp(10)

print(hero1.getHealth())