# multiple inheritance bisa nyebabin diamond problem
# misal kita punya class A
# lalu ada class B adalah child class A
# lalu ada class C adalah child class A
# lalu ada class D adalah child class A dan class B
# maka bentuk relasi keempat class tsb akan jd diamond problem
# misal di A ada method, terus di b methodnya di override, di c methodnya juga di override
# nah terus si d pake method yang mana? kalo methodnya sama itu masalahnya

class A:
    def method(self):
        print("method from A")


class B(A):
    def method(self):
        print("method  from B")


class C(A):
    def method(self):
        print("method from C")


class D(B, C):
    pass


d = D()
d.method()
