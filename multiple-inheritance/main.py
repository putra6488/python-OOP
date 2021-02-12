class A:

    def methodA(self):
        print("ini adalah method B")

class B:

    def methodB(self):
        print("ini adalah mmethod B")

# bisa mengambil sebuah banyak class
class C(A,B):
    pass

objek = C()

objek.methodA()
objek.methodB()