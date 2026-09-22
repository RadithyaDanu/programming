class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def bersuara(self):
        print("Suara hewan")


class Kucing(Hewan):
    def bersuara(self):          # Method Overriding
        print(f"{self.nama} mengeong: Meow!")

    def bermain(self):
        print(f"{self.nama} bermain bola")


kucing = Kucing("Mimi")
kucing.bersuara()   # Meow!
kucing.bermain()
