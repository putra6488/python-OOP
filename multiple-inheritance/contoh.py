# setiap hero member sebuah team dan memiliki tipe

class Team:
    def setTeam(self,team):
        self.team = team

    def showTeam(self):
        print(self.team)

class TipeHero:
    def setTipe(self, tipe):
        self.tipe = tipe

    def showTipe(self):
        print(self.tipe)

class Hero(Team, TipeHero):
    
    def __init__(self,name,health):
        self.name = name
        self.health = health

zilong = Hero("Zilong", 100)
zilong.setTeam("Merah")
zilong.setTipe("Fighter")
zilong.showTeam()
zilong.showTipe()