class Hero:

    # class variable
    jumlah = 0

    # private class var
    __privateJumlah = 0

    

    def __init__(self,name,health):
        self.name = name
        self.health = health

        # variable instance private
        self.__private = "private"

        # variable instance protected
        self._protected = "protected"

zilong = Hero("lina",100)
zilong._protected = "testing"
print(zilong.__dict__)