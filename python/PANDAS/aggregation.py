import pandas as pd

df = pd.read_csv("data.csv")

# mengubah set of value menjadi single summary value
# biasanya pake groupby
# aggregation gabisa kolom object, harus numerik (kecuali count)
# dipake buat analisis data

# aggregation entire data/whole dataframe
print(df.mean(numeric_only=True))  # sum,min,max sm aj

# aggregation by single column
print(df['Height'].mean())


# group by
# mengelompokkan data berdasarkan tipenya, misal dalam 1 kolom ada 3 tipe yaudah gitu
# kek di sql aja

group = df.groupby("Type1")
# setelah menggunakan aggregate, group mereturn tipe datanya jadi series
# series/ dataframe pemanggilannya pake []

print(group['Height'].mean())

# jadi disini kodenya berarti mencari mean dari height berdasarkan tipe2 dari isi si Type1
