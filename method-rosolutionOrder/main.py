# berhubungan dengan multiple inheritance

class A:
    
    def show(self):
        print("ini adalah show a")

class B:
    def show(self):
        print("ini adalah show b")

# class c adalah class yang akan di eksekusi terlebih dahulu
class C(A,B):
    pass

objek = C()

objek.show()

# untuk lihat urutan eksekusi
help(objek)