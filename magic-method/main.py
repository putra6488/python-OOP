# magic method = keywords yang bisa digunakan kembali
# contoh = __init__(), __repr__() dan banyak lagi, tandanya __

class Apel():

    # magic method
    def __init__(self,nama,jumlah):
        self.nama = nama
        self.jumlah = jumlah

    # di pakai saat debug
    def __repr__(self):
        return "debug: {}, jumlah: {}".format(self.nama, self.jumlah)

    # dipakai untuk program sudah jadi
    def __str__(self):
        return "apel: {}, jumlah: {}".format(self.nama, self.jumlah)

    # lebih ke aritmatika
    def __add__(self, objek):
        return self.jumlah + objek.jumlah

    @property
    def __dict__(self):
        return "objek memiliki jumlah dan nama"


beli = Apel("Apel", 10)
beli2 = Apel('Malang', 10)

print(repr(beli))
print(beli2)

print(beli + beli2)

# ini juga magic method
print(beli.__dict__)