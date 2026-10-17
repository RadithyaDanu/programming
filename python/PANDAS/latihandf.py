import pandas as pd

df = pd.read_csv("data.csv")
print(df)
# v1
new_data = pd.DataFrame({"No": [151, 152, 153, 154, 155],
                         "Name": ["a", "b", "c", "d", "e"],
                         "Type1": ["x1", "x2", "x3", "x4", "x5"],
                         "Type2": ["z1", "z2", "z3", "z4", "z5"],
                         "Height": [1, 2, 3, 4, 5],
                         "Weight": [5, 4, 3, 2, 1],
                         "Legendary": [1, 1, 1, 1, 1]},
                        index=["satu", "dua", "tiga", "empat", "lima"])

# v2
new_data2 = pd.DataFrame([
    {"No": 999, "Name": "a", "Type": "x99", "Type2": "z99", "Height": 99, "Weight": 99, "Legendary": 0}])
df = pd.concat([df, new_data])
print(f" ini data yang new_data 1\n {df.tail()}")

df = pd.concat([df, new_data2])
print(f"ini new data 1 + new data 2\n {df.tail()}")
