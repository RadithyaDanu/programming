import pandas as pd

df = pd.read_csv("data.csv")

# jadi konsep disini tuh kita panggil dataframe yg didalemnya terdapat kondisional series
print(df[df["Weight"] > 2])
# jadi data yang ditampilkan berisi kondisional series(df[weight] yang lebih dari 2)
# berlaku ke semua jenis, type string berarti masukin namanya

# logical filtering
# logical filtering harus dibungkus sama () diantara kondisionalnya
# or |, and &
# gitulah doang
print(df[(df['Weight'] > 10) or (df['Height'] > 2)])