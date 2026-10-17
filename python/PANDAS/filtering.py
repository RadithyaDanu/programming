import pandas as pd

df = pd.read_csv("data.csv")

# jadi konsep disini tuh kita panggil dataframe yg didalemnya terdapat kondisional series
print(df[df["Weight"] > 2])
