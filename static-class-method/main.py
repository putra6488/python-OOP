class Hero:
    # ?private variable
    __jumlah = 0

    def __init__(self,name):
        self.__name = name
        Hero.__jumlah += 1

    # method ini hanya untuk objek
    def getJumlah(self):
        return Hero.__jumlah

    # method ini tidak untuk objek tapi bisa untuk class
    def getJumlah1():
        return Hero.__jumlah

    # static method (decorator)
    @staticmethod
    def getJumlah2():
        return Hero.__jumlah

    # bisa ambil argumen
    @classmethod
    def getJumlah3(cls):
        return cls.__jumlah


miya = Hero('miya')
print(Hero.getJumlah2())

layla = Hero('layla')
print(miya.getJumlah2())

zilong = Hero('zilong')
print(miya.getJumlah3())