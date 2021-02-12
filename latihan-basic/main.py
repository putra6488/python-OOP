# hero: nama, health, att power, deff power

class Hero:

    def __init__(self, name, health, attackPower, armor):
        self.name = name
        self.health = health
        self.attackPower = attackPower
        self.armor = armor

    def serang(self, lawan):
        print(self.name + ' menyerang ' + lawan.name)
        lawan.diserang(self, self.attackPower)

    def diserang(self, lawan, attackPowerLawan):
        print(self.name + ' di serang ' + lawan.name)
        attackDiterima = attackPowerLawan/self.armor
        print('serang terasa : ' + str(attackDiterima))
        self.health -= attackDiterima
        print('darah ' + self.name + ' tersisa :  ' + str(self.health))

miya = Hero('Miya', 100, 10, 5)
layla = Hero('Layla', 100, 20, 10)

miya.serang(layla)
print(20*'=')
layla.serang(miya)
miya.serang(layla)
print(20*'=')
layla.serang(miya)
miya.serang(layla)
print(20*'=')
layla.serang(miya)
miya.serang(layla)
print(20*'=')
layla.serang(miya)