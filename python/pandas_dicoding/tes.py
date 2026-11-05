import pandas as pd

# merge antara dataset
# inner join = ngambil data yang bersesuaian
# left join = ngambil semua data kiri dan ambil yang bersesuaian di data kanan
# right join = kebalikan left join
# outer = gabungin semua

price = pd.read_csv("price.csv")
product = pd.read_csv("product.csv")

# setelah data di baca oleh python
# product id merupakan primary key dari product dan foreign key dari price
# declare sisi kiri dan kanan dari dataset, lalu tentukan bagaimana data mau di merge
# habis itu tentuin pk dan fk
df_merge = pd.merge(
    left=product,
    right=price,
    how="inner",
    left_on="product_id",
    right_on="product_id"
)

print(df_merge)
