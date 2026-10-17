import pandas as pd

calories = {"day 1": 1700, "day 2 ": 1900, "day 3": 2000}

series = pd.Series(calories)
print(series)
print(f"series day1 {series['day 1']}")
# karena dict bersifat key-value, maka gaperlu bikin index di seriesnya
# key otomatis mengikuti pada dict

# kita tambahin 300 pada day 3
series.loc['day 3'] += 500
print(f"hasil nambah 500 di  day 3 : {series['day 3']}")
