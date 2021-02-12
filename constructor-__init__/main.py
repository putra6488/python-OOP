class Hero:

    jumlah = 0

    # pertama kali dijalankan
    def __init__(self, inputName, inputPower, inputArmor, inputHealth):
        # instance variable
        self.name = inputName
        self.power = inputPower
        self.armor = inputArmor
        self.health = inputHealth
        Hero.jumlah += 1
        print("membuat nama dengan nama : " + inputName)


hero1 = Hero("Miya", 100, 10, 4)
print(Hero.jumlah)
hero2 = Hero("Layla", 90, 10, 3)
print(Hero.jumlah)
hero3 = Hero("Gatot", 500, 40, 9)
print(Hero.jumlah)