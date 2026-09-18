# fitur alternatif yang lebih bersih untuk else if yang banyak
# semakin banyak semakin susah dibacanya kalo pake elif

hari = input("masukkan nama hari : ").lower()

if hari == "senin" or hari == "selasa" or hari == "rabu" or hari == "kamis" or hari == "jumat":
    print(f"{hari} adalah hari kerja")
elif hari == "sabtu" or hari == "minggu":
    print(f"{hari} adalah hari libur")
else:
    print(f"{hari} bukan nama hari yang valid")

# match case
match hari:
    case "senin" | "selasa" | "rabu" | "kamis" | "jumat":
        print(f"{hari} adalah hari kerja")
    case "sabtu" | "minggu":
        print(f"{hari} adalah hari libur")
    case _:
        print(f"{hari} bukan nama hari yang valid")
