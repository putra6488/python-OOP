class Hero:

    def __init__(self, name, health, armor):
        self.name = name
        self.__health = health
        self.__armor = armor
        # self.info = "name {} : \n\thealth: {}".format(self.__name,self.__health)

    @property
    def info(self):
        return  "name {} : \n\thealth: {}".format(self.name,self.__health)

    @property
    def armor(self):
        pass

    # getter
    @armor.getter
    def armor(self):
        return self.__armor

    # setter
    @armor.setter
    def armor(self, input):
        self.__armor = input

     # deleter
    @armor.deleter
    def armor(self):
        print("armor di delete")
        self.__armor = None



miya = Hero("miya", 100, 10)

print("merubah info")
print(miya.info)
miya.name = "niku"
print(miya.info)

print("getter and setter untuk __armor : ")
print(miya.armor)

print("delete armor")
del miya.armor
print(miya.__dict__)