from hero import Hero_mage,Hero_tank

kagura = Hero_mage("Kagura")
lolita = Hero_tank("Lolita")

kagura.showInfo()
lolita.showInfo()

kagura.gainExp = 200
lolita.gainExp = 300

kagura.showInfo()
lolita.showInfo()