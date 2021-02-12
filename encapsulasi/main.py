# getter = ambil varible
# setter = setting variable

class Hero:

    def __init__(self,name,health,attPower):
        self.__name = name
        self.__health = health
        self.__attPower = attPower

    # getter
    def getName(self):
        return self.__name

    def getHealth(self):
        return self.__health

    # setter
    def diserang(self, serangPower):
        self.__health -= serangPower

    def setAttPow(self,nilaiBaru):
        self.__attPower = nilaiBaru

# awal
alu = Hero("Alucard", 100, 200)

# berjalan
print(alu.getName())
print(alu.getHealth())
alu.diserang(20)
print(alu.getHealth())