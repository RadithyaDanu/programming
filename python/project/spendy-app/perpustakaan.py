from abc import ABC, abstractmethod
from datetime import datetime, timedelta


class Item(ABC):
    """Abstract class untuk semua item di perpustakaan"""

    def __init__(self, judul, tahun):
        self._judul = judul
        self._tahun = tahun
        self._tersedia = True

    @property
    def judul(self):
        return self._judul

    @property
    def tersedia(self):
        return self._tersedia

    def pinjam(self):
        if self._tersedia:
            self._tersedia = False
            return True
        return False

    def kembalikan(self):
        self._tersedia = True

    @abstractmethod
    def info(self):
        """Setiap subclass wajib mengimplementasikan method ini"""
        pass


class Buku(Item):
    def __init__(self, judul, tahun, pengarang, isbn):
        super().__init__(judul, tahun)
        self.__pengarang = pengarang
        self.__isbn = isbn

    def info(self):
        status = "Tersedia" if self._tersedia else "Dipinjam"
        return (f"[Buku] {self._judul} ({self._tahun}) | "
                f"Pengarang: {self.__pengarang} | "
                f"ISBN: {self.__isbn} | Status: {status}")


class Majalah(Item):
    def __init__(self, judul, tahun, edisi):
        super().__init__(judul, tahun)
        self.__edisi = edisi

    def info(self):
        status = "Tersedia" if self._tersedia else "Dipinjam"
        return (f"[Majalah] {self._judul} - Edisi {self.__edisi} "
                f"({self._tahun}) | Status: {status}")


class Member:
    def __init__(self, nama, id_member):
        self.nama = nama
        self.id_member = id_member
        self.__daftar_pinjaman = []  # encapsulation

    def pinjam_item(self, item):
        if item.pinjam():
            tanggal_kembali = datetime.now() + timedelta(days=7)
            self.__daftar_pinjaman.append({
                "item": item,
                "batas_waktu": tanggal_kembali
            })
            print(f"{self.nama} berhasil meminjam '{item.judul}'")
            print(
                f"Batas pengembalian: {tanggal_kembali.strftime('%d-%m-%Y')}")
            return True
        else:
            print(f"Maaf, '{item.judul}' sedang dipinjam orang lain")
            return False

    def kembalikan_item(self, item):
        for pinjaman in self.__daftar_pinjaman:
            if pinjaman["item"] == item:
                item.kembalikan()
                self.__daftar_pinjaman.remove(pinjaman)
                print(f" {self.nama} berhasil mengembalikan '{item.judul}'")
                return True
        print(f" {self.nama} tidak meminjam item tersebut")
        return False

    def lihat_pinjaman(self):
        if not self.__daftar_pinjaman:
            print(f"{self.nama} tidak memiliki pinjaman aktif")
            return
        print(f"\nDaftar pinjaman {self.nama}:")
        for p in self.__daftar_pinjaman:
            print(
                f"  - {p['item'].judul} | Batas: {p['batas_waktu'].strftime('%d-%m-%Y')}")


class Perpustakaan:
    def __init__(self, nama):
        self.nama = nama
        self.__koleksi = []  # list of item
        self.__members = []  # list of member

    def tambah_item(self, item):
        self.__koleksi.append(item)
        print(f"+ Item '{item.judul}' ditambahkan ke koleksi")

    def daftar_member(self, member):
        self.__members.append(member)
        print(f"+ Member '{member.nama}' berhasil didaftarkan")

    def cari_item(self, kata_kunci):
        hasil = [item for item in self.__koleksi if kata_kunci.lower()
                 in item.judul.lower()]
        return hasil

    def tampilkan_semua_item(self):
        print(f"\n===Koleksi {self.nama}===")
        if not self.__koleksi:
            print("Belum ada item")
            return
        for i, item in enumerate(self.__koleksi, 1):
            print(f"{i}. {item.info()}")  # polymorphism

    def tampilkan_members(self):
        print(f"\n=== Daftar Member {self.nama} ===")
        for m in self.__members:
            print(f"- {m.nama} (ID: {m.id_member})")

    @staticmethod
    def info_peraturan():
        print("\n===Peraturan Perpustakaan===")
        print("1. Maksimal pinjam 7 hari")
        print("2. Denda keterlambatan Rp 2000/hari")
        print("3. Harus mengembalikan sebelum meminjam item baru")


def main():
    perpus = Perpustakaan("Perpustakaan Kota Python")

    buku1 = Buku("Python Crash Course", 2023, "Eric Matthes", "978-1593279288")
    buku2 = Buku("Clean Code", 2008, "Robert C. Martin", "978-0132350884")
    majalah1 = Majalah("National Geographic", 2024, "Edisi Januari")
    majalah2 = Majalah("Tempo", 2024, "Edisi 15")

    perpus.tambah_item(buku1)
    perpus.tambah_item(buku2)
    perpus.tambah_item(majalah1)
    perpus.tambah_item(majalah2)

    andi = Member("Andi Pratama", "M001")
    siti = Member("Siti Aminah", "M002")

    perpus.daftar_member(andi)
    perpus.daftar_member(siti)

    perpus.tampilkan_semua_item()

    print("\n---Proses Peminjaman---")
    andi.pinjam_item(buku1)
    andi.pinjam_item(majalah1)
    siti.pinjam_item(buku1)

    andi.lihat_pinjaman()
    siti.lihat_pinjaman()

    print("\n---Proses Pengembalian---")
    andi.kembalikan_item(buku1)
    siti.pinjam_item(buku1)

    perpus.tampilkan_semua_item()

    Perpustakaan.info_peraturan()


if __name__ == "__main__":
    main()
