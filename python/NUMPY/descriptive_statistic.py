import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# data = np.array([1, 5, 7, 8, 9, 9, 6, 4, 3, 5, 7, 8, 7])
# print(f"mean = {data.mean()}")
# # print(f"median = {data.median()}")
# print(np.median(data))

# range_data = data.max() - data.min()
# print(range_data)

# # rumus iqr = q3-q1
# iqr = np.percentile(data, 75) - np.percentile(data, 25)
# print(iqr)

# # variance
# # ubah ke series dulu
# variance = pd.Series(data)
# print(variance.var())

# # standar deviation
# standar_deviation = variance
# print(f"sd = {standar_deviation.std()}")


# # plt.hist(data, bins=4)
# # plt.show()


print("===============data relationship====================")
sample_data = {
    'name': ['John', 'Alia', 'Ananya', 'Steve', 'Ben'],
    'age': [24, 22, 23, 25, 28],
    'communication_skill_score': [85, 70, 75, 90, 90],
    'quantitative_skill_score': [80, 90, 80, 75, 70]
}
df = pd.DataFrame(sample_data)
print(df.corr(numeric_only=True))
